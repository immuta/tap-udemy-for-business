"""REST client handling, including UdemyForBusinessStream base class."""

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

    def get_next_page_token(
        self, response: requests.Response, previous_token: Optional[Any] = None
    ) -> Optional[Any]:
        """Return a token for identifying next page or None if no more pages."""

        try:
            next_page_url = response.json()["next"]
            match = re.search("page=([0-9]+)", next_page_url)
            if match:
                next_page_token = int(match.group(1))
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

    def post_process(self, row: dict, context: Optional[dict] = None) -> dict:
        if row.get("user_email") != "Anonymized User":
            return None
        if any(row.get(k) == None for k in self.primary_keys):
            return None
        return row
