"""REST client handling, including UdemyForBusinessStream base class."""

import base64
import requests

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk.streams import RESTStream


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class UdemyForBusinessStream(RESTStream):
    """UdemyForBusiness stream class."""

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://{}.udemy.com/api-2.0/organizations/{}".format(
            self.config['organization_name'],
            self.config['organization_id']
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        # Authentication
        raw_credentials = f"{self.config['client_id']}:{self.config['client_secret']}"
        auth_token = base64.b64encode(raw_credentials.encode()).decode('ascii')
        headers["Authorization"] = f"Basic {auth_token}"

        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any] = None
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""
        # TODO: If pagination is required, return a token which can be used to get the
        #       next page. If this is the final page, return "None" to end the
        #       pagination loop.
        next_page_token = response.headers.get("X-Next-Page", None)
        if next_page_token:
            self.logger.info(f"Next page token retrieved: {next_page_token}")
        return next_page_token


    # {
    # "count": 19573,
    # "next": "https://immuta.udemy.com/api-2.0/organizations/116724/analytics/user-progress/?page=2",
    # "previous": null,
    # "results": [


    def get_url_params(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params: dict = {}
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params

    def prepare_request_payload(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Optional[dict]:
        """Prepare the data payload for the REST API request.

        By default, no payload will be sent (return None).
        """
        # TODO: Delete this method if no payload is required. (Most REST APIs.)
        return None

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        resp_json = response.json()
        for row in resp_json.get("results"):
            yield row

