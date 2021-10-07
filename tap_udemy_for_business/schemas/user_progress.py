from singer_sdk import typing as th


th.PropertiesList(
    th.Property("user_email", th.StringType, required=True),
    th.Property("course_id", th.IntegerType, required=True),
    th.Property("item_id", th.IntegerType, required=True),
    th.Property("_class", th.StringType),
    th.Property("user_external_id", th.StringType),
    th.Property("course_title", th.StringType),
    th.Property("item_title", th.StringType),
    th.Property("user_name", th.StringType),
    th.Property("user_surname", th.StringType),
    th.Property("user_role", th.StringType),
    th.Property("user_is_deactivated", th.BooleanType),
    th.Property("item_type", th.StringType),
    th.Property("item_start_time", th.DateTimeType),
    th.Property("item_completion_time", th.DateTimeType),
    th.Property("item_views", th.NumberType),
    th.Property("item_completion_ratio", th.NumberType),
    th.Property("item_final_result", th.NumberType),
    th.Property("item_marked_complete", th.BooleanType),
    th.Property("course_category", th.StringType),
).to_dict()
