"""UdemyForBusiness Authentication."""
import base64

from singer_sdk.authenticators import SimpleAuthenticator


class UdemyForBusinessAuthenticator(SimpleAuthenticator):
    """Authenticator class for UdemyForBusiness."""

    @classmethod
    def create_for_stream(cls, stream) -> "UdemyForBusinessAuthenticator":
        raw_credentials = f"{stream.config['client_id']}:{stream.config['client_secret']}"
        auth_token = base64.b64encode(raw_credentials.encode()).decode('ascii')
        return cls(
            stream=stream,
            auth_headers={
                "Authorization": f"Basic {auth_token}"
            }
        )
