"""Stream type classes for tap-udemy-for-business."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_udemy_for_business.client import UdemyForBusinessStream

# from_date = "2021-03-24" will filter

class CoursesStream(UdemyForBusinessStream):
    name = "courses"
    path = "/courses/list"
    primary_keys = ["id"]
    replication_key = "last_update_date"

    schema =  th.PropertiesList(
        th.Property("_class", th.StringType),
        th.Property("id", th.IntegerType), # Course Id, this is a unique identifier for the course
        th.Property("title", th.StringType), # Course Title, this is the title of the course	
        th.Property("description", th.StringType), # Course Description, this is the description of the course
        th.Property("url", th.StringType), # This is a URL pointing to the course's web location
        th.Property("estimated_content_length", th.IntegerType), # Estimated Content Length, this is an estimated length of time the content would take to be consumed
        th.Property("num_lectures", th.IntegerType), # Number of Lectures, the number of lectures this course comprises of	
        th.Property("num_videos", th.IntegerType), # Number of Videos, the number of videos contained in this course	
        th.Property("mobile_native_deeplink", th.StringType), # Mobile Native Deeplink. This URL will open the course in the Udemy for Business native app for Android or iOS, if installed	
        th.Property("is_practice_test_course", th.BooleanType),
        th.Property("num_quizzes", th.IntegerType), # Number of quizzes contained in the course	
        th.Property("num_practice_tests", th.IntegerType), # Number of practice tests contained in the course
        th.Property("has_closed_caption", th.BooleanType),
        th.Property("estimated_content_length_video", th.IntegerType),
        th.Property("last_update_date", th.DateTimeType),
        th.Property("xapi_activity_id", th.StringType),
        th.Property("caption_languages", th.ArrayType(th.StringType)),
        th.Property("caption_locales", th.ArrayType(th.StringType)),
        th.Property("categories", th.ArrayType(th.StringType)), # Category, this is a list of categories into which this course fits	
        th.Property("instructors", th.ArrayType(th.StringType)), # Instructor Names, a list of the instructor names for the course	
        th.Property("requirements", th.ObjectType(
            th.Property("list", th.ArrayType(th.StringType))
        )), # Requirements, a description of requirements for this course	
        th.Property("images", th.ObjectType(
            th.Property("size_100x100", th.StringType)
        )), # Course Image Urls, a list of sizes and urls pointing to the course image locations
        th.Property("what_you_will_learn", th.ObjectType(
            th.Property("list", th.ArrayType(th.StringType))
        )), # What you will learn, a description of the skills and knowledge which will be learned on this course	
        th.Property("locale",  th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("locale", th.StringType)
        )), # Indicates the language of the course (e.g. es_ES)	
        th.Property("primary_category", th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("id", th.IntegerType),
            th.Property("title", th.StringType),
            th.Property("url", th.StringType)
        )),
        th.Property("primary_subcategory", th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("id", th.IntegerType),
            th.Property("title", th.StringType),
            th.Property("url", th.StringType)
        )),
        th.Property("promo_video_url", th.ArrayType(
            th.ObjectType(
                th.Property("type", th.StringType),
                th.Property("label", th.StringType),
                th.Property("file", th.StringType),
            )
        )) # Promotional Video Url, the url of the promotional video	
    ).to_dict()


class UserActivityStream(UdemyForBusinessStream):
    name = "user_activity"
    path = "/analytics/user-activity"
    primary_keys = ["user_email"]
    replication_key = "last_date_visit"

    schema = th.PropertiesList(
        th.Property("user_name", th.StringType),
        th.Property("user_surname", th.StringType),
        th.Property("user_email", th.StringType),
        th.Property("user_role", th.StringType),
        th.Property("user_joined_date", th.DateTimeType),
        th.Property("user_external_id", th.StringType),
        th.Property("user_is_deactivated", th.BooleanType),
        th.Property("num_new_enrolled_courses", th.IntegerType),
        th.Property("num_new_assigned_courses", th.IntegerType),
        th.Property("num_new_started_courses", th.IntegerType),
        th.Property("num_completed_courses", th.IntegerType),
        th.Property("num_completed_lectures", th.IntegerType),
        th.Property("num_completed_quizzes", th.IntegerType),
        th.Property("num_video_consumed_minutes", th.NumberType),
        th.Property("num_web_visited_days", th.IntegerType),
        th.Property("last_date_visit", th.DateTimeType),
    ).to_dict()


class UserCourseActivityStream(UdemyForBusinessStream):
    name = "user_course_activity"
    path = "/analytics/user-course-activity"
    primary_keys = ["user_email", "course_id"]

    schema = th.PropertiesList(
        th.Property("user_name", th.StringType),
        th.Property("user_surname", th.StringType),
        th.Property("user_email", th.StringType),
        th.Property("user_role", th.StringType),
        th.Property("user_external_id", th.StringType),
        th.Property("course_id", th.IntegerType),
        th.Property("course_title", th.StringType),
        th.Property("course_category", th.StringType),
        th.Property("course_duration", th.NumberType),
        th.Property("completion_ratio", th.NumberType),
        th.Property("num_video_consumed_minutes", th.NumberType),
        th.Property("course_enroll_date", th.DateTimeType),
        th.Property("course_start_date", th.StringType),
        th.Property("course_completion_date", th.StringType),
        th.Property("course_first_completion_date", th.StringType),
        th.Property("course_last_accessed_date", th.DateTimeType),
        th.Property("is_assigned", th.BooleanType),
        th.Property("assigned_by", th.StringType),
        th.Property("user_is_deactivated", th.BooleanType),
        th.Property("lms_user_id", th.StringType),
    ).to_dict()
 

class UserProgressStream(UdemyForBusinessStream):
    name = "user_progress"
    path = "/analytics/user-progress"
    primary_keys = ["id"]
    schema = th.PropertiesList(
        th.Property("_class", th.StringType),
        th.Property("id", th.IntegerType),
        th.Property("user_email", th.StringType),
        th.Property("course_id", th.IntegerType),
        th.Property("course_title", th.StringType),
        th.Property("item_title", th.StringType),
        th.Property("user_name", th.StringType),
        th.Property("user_surname", th.StringType),
        th.Property("user_role", th.StringType),
        th.Property("user_is_deactivated", th.BooleanType),
        th.Property("item_type", th.StringType),
        th.Property("item_id", th.IntegerType),
        th.Property("item_start_time", th.DateTimeType),
        th.Property("item_completion_time", th.DateTimeType),
        th.Property("item_views", th.NumberType),
        th.Property("item_completion_ratio", th.NumberType),
        th.Property("item_final_result", th.StringType),
        th.Property("item_marked_complete", th.BooleanType),
        th.Property("course_category", th.StringType)       
    ).to_dict()

    def get_url_params(
        self, partition: Optional[dict], next_page_token: Optional[Any] = None
    ) -> Dict[str, Any]:
        params = {
            "page_size": 1000,
            "from_date": self.config.get("start_date")
        }
        if next_page_token:
            params["page"] = next_page_token
        if self.replication_key:
            params["sort"] = "asc"
            params["order_by"] = self.replication_key
        return params