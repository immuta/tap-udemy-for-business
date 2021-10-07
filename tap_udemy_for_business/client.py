"""REST client handling, including UdemyForBusinessStream base class."""

import base64
import requests
import re

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable
from singer_sdk.streams import RESTStream
from singer_sdk.authenticators import BasicAuthenticator
from singer_sdk.helpers.jsonpath import extract_jsonpath


SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class UdemyForBusinessStream(RESTStream):
    """UdemyForBusiness stream class."""

    _page_size = 1000
    records_jsonpath = "$.results[*]"

    @property
    def url_base(self) -> str:
        """Return the API URL root, configurable via tap settings."""
        return "https://{}.udemy.com/api-2.0/organizations/{}".format(
            self.config["organization_name"], self.config["organization_id"]
        )

    @property
    def authenticator(self):
        return BasicAuthenticator.create_for_stream(
            self,
            username=self.config["client_id"],
            password=self.config["client_secret"],
        )

    @property
    def http_headers(self) -> dict:
        """Return the http headers needed."""
        headers = {}
        if "user_agent" in self.config:
            headers["User-Agent"] = self.config.get("user_agent")

        raw_credentials = f"{self.config['client_id']}:{self.config['client_secret']}"
        auth_token = base64.b64encode(raw_credentials.encode()).decode("ascii")
        headers["Authorization"] = f"Basic {auth_token}"

        return headers

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any] = None
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        try:
            next_page_url = response.json()["next"]
            self.logger.info(next_page_url)
            match = re.search("page=([0-9]+)", next_page_url)
            if match:
                next_page_token = int(match.group(1))
                self.logger.info(f"Next page token retrieved: {next_page_token}")
                return next_page_token
        except KeyError:
            return None
        except TypeError:
            return None

    def get_url_params(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        """Return a dictionary of values to be used in URL parameterization."""
        params = {"page_size": self._page_size}
        if next_page_token:
            params["page"] = next_page_token
        return params

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
        """Parse the response and return an iterator of result rows."""
        yield from [
            row
            for row in extract_jsonpath(self.records_jsonpath, input=response.json())
            if row.get("user_email") != "Anonymized User"
            and all(row.get(k) is not None for k in self.primary_keys)
        ]
