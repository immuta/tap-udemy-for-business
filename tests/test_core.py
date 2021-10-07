"""Tests standard tap features using the built-in SDK tests library."""

import datetime
import os

from singer_sdk.testing import get_standard_tap_tests

from tap_udemy_for_business.tap import TapUdemyForBusiness

SAMPLE_CONFIG = {
    "start_date": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d"),
    "client_id": os.environ.get("CLIENT_ID", "myClientId"),
    "client_secret": os.environ.get("CLIENT_SECRET", "myClientSecret"),
    "organization_name": os.environ.get("ORGANIZATION_NAME", "myOrganization"),
    "organization_id": int(os.environ.get("ORGANIZATION_ID", 99999)),
}


# Run standard built-in tap tests from the SDK:
def test_standard_tap_tests():
    """Run standard tap tests from the SDK."""
    tests = get_standard_tap_tests(TapUdemyForBusiness, config=SAMPLE_CONFIG)
    for test in tests:
        test()
