"""UdemyForBusiness tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_udemy_for_business.streams import (
    CoursesStream,
    UserActivityStream,
    UserCourseActivityStream,
    UserProgressStream,
)

STREAM_TYPES = [
    CoursesStream,
    UserActivityStream,
    UserCourseActivityStream,
    UserProgressStream,
]


class TapUdemyForBusiness(Tap):
    """UdemyForBusiness tap class."""

    name = "tap-udemy-for-business"

    config_jsonschema = th.PropertiesList(
        th.Property("client_id", th.StringType, required=True),
        th.Property("client_secret", th.StringType, required=True),
        th.Property("organization_id", th.IntegerType, required=True),
        th.Property("organization_name", th.StringType, required=True),
        th.Property("start_date", th.DateTimeType),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
