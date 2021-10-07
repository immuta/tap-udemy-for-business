"""Stream type classes for tap-udemy-for-business."""

from dateutil import parser
from typing import Any, Dict, Optional, Union, List, Iterable

from tap_udemy_for_business.client import UdemyForBusinessStream
from tap_udemy_for_business import schemas


class CoursesStream(UdemyForBusinessStream):
    name = "courses"
    path = "/courses/list"
    primary_keys = ["id"]
    _page_size = 100
    schema = schemas.courses

    def get_url_params(self, partition, next_page_token) -> Dict:
        "Overwrite SDK method to request specific fields from the endpoint."
        params = super().get_url_params(partition, next_page_token)
        params["fields[course]"] = ",".join(
            [
                "_class",
                "id",
                "title",
                "description",
                "url",
                "estimated_content_length",
                "num_lectures",
                "num_videos",
                "mobile_native_deeplink",
                "is_practice_test_course",
                "num_quizzes",
                "num_practice_tests",
                "has_closed_caption",
                "estimated_content_length_video",
                "last_update_date",
            ]
        )
        return params


class UserActivityStream(UdemyForBusinessStream):
    name = "user_activity"
    path = "/analytics/user-activity"
    primary_keys = ["user_email"]
    schema = schemas.user_activity


class UserCourseActivityStream(UdemyForBusinessStream):
    name = "user_course_activity"
    path = "/analytics/user-course-activity"
    primary_keys = ["user_email", "course_id"]
    schema = schemas.user_course_activity


class UserProgressStream(UdemyForBusinessStream):
    name = "user_progress"
    path = "/analytics/user-progress"
    primary_keys = ["user_email", "course_id", "item_id"]
    schema = schemas.user_progress

    def get_url_params(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        "Overwrite SDK method to allow `from_date` to be passed in."
        params = super().get_url_params(partition, next_page_token=next_page_token)
        params["from_date"] = self.get_starting_timestamp(context=partition).strftime("%Y-%m-%d")
        return params
