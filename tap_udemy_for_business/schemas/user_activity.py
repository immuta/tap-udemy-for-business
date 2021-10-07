from singer_sdk import typing as th


th.PropertiesList(
    th.Property("user_email", th.StringType, required=True),
    th.Property("user_name", th.StringType),
    th.Property("user_surname", th.StringType),
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
