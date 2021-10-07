from singer_sdk import typing as th


th.PropertiesList(
    th.Property("course_id", th.IntegerType, required=True),
    th.Property("user_email", th.StringType, required=True),
    th.Property("user_name", th.StringType),
    th.Property("user_surname", th.StringType),
    th.Property("user_role", th.StringType),
    th.Property("user_external_id", th.StringType),
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
