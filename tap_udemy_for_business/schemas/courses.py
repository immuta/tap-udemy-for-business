from singer_sdk import typing as th


schema = th.PropertiesList(
    th.Property("_class", th.StringType),
    th.Property(
        "id",
        th.IntegerType,
        description="Course Id, this is a unique identifier for the course",
    ),
    th.Property(
        "title",
        th.StringType,
        description="Course Title, this is the title of the course",
    ),
    th.Property(
        "description",
        th.StringType,
        description="Course Description, this is the description of the course",
    ),
    th.Property(
        "url",
        th.StringType,
        description="This is a URL pointing to the course's web location",
    ),
    th.Property(
        "estimated_content_length",
        th.IntegerType,
        description="Estimated Content Length, this is an estimated length of time the content would take to be consumed",
    ),
    th.Property(
        "num_lectures",
        th.IntegerType,
        description="Number of Lectures, the number of lectures this course comprises of",
    ),
    th.Property(
        "num_videos",
        th.IntegerType,
        description="Number of Videos, the number of videos contained in this course",
    ),
    th.Property(
        "mobile_native_deeplink",
        th.StringType,
        description="Mobile Native Deeplink. This URL will open the course in the Udemy for Business native app for Android or iOS, if installed",
    ),
    th.Property("is_practice_test_course", th.BooleanType),
    th.Property(
        "num_quizzes",
        th.IntegerType,
        description="Number of quizzes contained in the course",
    ),
    th.Property(
        "num_practice_tests",
        th.IntegerType,
        description="Number of practice tests contained in the course",
    ),
    th.Property("has_closed_caption", th.BooleanType),
    th.Property("estimated_content_length_video", th.IntegerType),
    th.Property("last_update_date", th.DateTimeType),
    th.Property("xapi_activity_id", th.StringType),
    th.Property("caption_languages", th.ArrayType(th.StringType)),
    th.Property("caption_locales", th.ArrayType(th.StringType)),
    th.Property(
        "categories",
        th.ArrayType(th.StringType),
        description="Category, this is a list of categories into which this course fits",
    ),
    th.Property(
        "instructors",
        th.ArrayType(th.StringType),
        description="Instructor Names, a list of the instructor names for the course",
    ),
    th.Property(
        "requirements",
        th.ObjectType(th.Property("list", th.ArrayType(th.StringType))),
        description="Requirements, a description of requirements for this course",
    ),
    th.Property(
        "images",
        th.ObjectType(th.Property("size_100x100", th.StringType)),
        description="Course Image Urls, a list of sizes and urls pointing to the course image locations",
    ),
    th.Property(
        "what_you_will_learn",
        th.ObjectType(th.Property("list", th.ArrayType(th.StringType))),
        description="What you will learn, a description of the skills and knowledge which will be learned on this course",
    ),
    th.Property(
        "locale",
        th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("locale", th.StringType),
            th.Property(),
        ),
        description="Indicates the language of the course (e.g. es_ES)",
    ),
    th.Property(
        "primary_category",
        th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("id", th.IntegerType),
            th.Property("title", th.StringType),
            th.Property("url", th.StringType),
        ),
    ),
    th.Property(
        "primary_subcategory",
        th.ObjectType(
            th.Property("_class", th.StringType),
            th.Property("id", th.IntegerType),
            th.Property("title", th.StringType),
            th.Property("url", th.StringType),
        ),
    ),
    th.Property(
        "promo_video_url",
        th.ArrayType(
            th.ObjectType(
                th.Property("type", th.StringType),
                th.Property("label", th.StringType),
                th.Property("file", th.StringType),
            )
        ),
        description="Promotional Video Url, the url of the promotional video",
    ),
).to_dict()
