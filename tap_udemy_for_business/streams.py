"""Stream type classes for tap-udemy-for-business."""

from pathlib import Path
from typing import Any, Dict, Optional, Union, List, Iterable

from singer_sdk import typing as th  # JSON Schema typing helpers
from tap_udemy_for_business.client import UdemyForBusinessStream


# class CoursesStream(UdemyForBusinessStream):
#     name = "courses"
#     path = "/courses/list"
# {
#     "count": 10328,
#     "next": "https://immuta.udemy.com/api-2.0/organizations/116724/courses/list/?page=2",
#     "previous": null,
#     "results": [
#         {
            # th.Propert("_class", th.StringType),      : "course",
            # th.Propert("id", th.IntegerType),      : 900920,
            # th.Propert("title", th.StringType),      : "〜デザイナーの頭の中、大公開〜　企画を「１枚の紙」で、伝えきる。",
            # th.Propert("description", th.StringType),      : "<p><strong><em>また企画が通らなかった…。</em></strong></p>\n\n<p><strong><em>たくさんデータを分析して考えたのに、なぜかユーザーに響かない…。</em></strong></p>\n\n<p><strong><em>企画書を作っているうちに、何が大事なのかわからなくなってしまいがち…。</em></strong></p>\n\n<p><br></p>\n\n<p>デザイナー、アートディレクターとして仕事をしていると、このような悩みをお持ちのかたから依頼をいただくことがあります。</p>\n\n<p>企画に対する悩みや迷いをときほぐしながら一緒にアウトプットを考えていくのですが、<strong>企画を「１枚の紙」にまとめる</strong>ことで、大事なポイントがスッキリし、ぐんとアイデアを考えやすくなります。</p>\n\n<p>この講座では、僕が実際に過去に担当させていただいた、３つのケースに一緒に取り組みながら、企画を「１枚の紙」にまとめる練習をしていきます。毎回一般のゲストをお招きして、「デザイナーチーム」としてケースに挑みます。</p>\n\n<p><strong>　ケース１：温泉宿の売上を増やすには？（箱根　匠の宿　佳松さんからのご依頼）</strong></p>\n\n<p><strong>　ケース２：JR時刻表の表紙で、50周年を盛り上げるには？（交通新聞社さんからのご依頼）</strong></p>\n\n<p><strong>　ケース３：植物標本を１万円で売るには？（PLANTS TRADEさんからのご依頼）</strong></p>\n\n<p>デザイナーやアートディレクターのの考え方にふれ、明日からのご自身の仕事に何か１つでも新しい視点を取り入れていただけるといいなと願っています。</p>\n\n<p>「デザイナーチーム」の一員としてワークショップに参加した気分で、楽しく受講していただけたら幸いです。</p>",
            # th.Propert("url", th.StringType),      : "https://immuta.udemy.com/course/triplet_design/",
            # th.Propert("estimated_content_length", th.IntegerType),      : 178,
            # th.Propert("categories", th.StringType),      : ["Marketing Strategy"],
            # th.Propert("num_lectures", th.IntegerType),      : 26,
            # th.Propert("num_videos", th.IntegerType),      : 26,
            # th.Propert("promo_video_url", th.ArrayType),      : [    {        "type": "video/mp4",        "label": "720",        "file": "https://mp4-c.udemycdn.com/2016-08-08_02-16-31-087b2a57c7d2372b771a6feade86278c/WebHD_720p.mp4?Expires=1621313644&Signature=Hs78~UcWhg9s802ZVEJVHAneGhUAioFChii68QRKr8Hr7GJ5YXgNg4LXlHG2MdN5ZdK9rSFP~pD0qK4tM5iNxDGNkXaxpKGYXY7T1tAXH-rL0S6iwS4xN9uUJite~rK9h5of2JmWn14NmjiAdL1foZwXgTM7TWz6rt6jUyYpnsxSF6Am-ajmGka6xZlL01LazAiQa0hb7e9SRjlcbf~0ql-VaSrDrRZeS86JmAtDdL4RqaB5aPvc7Tgkvb~8Y~pNlsGUZeCd47nFHLo6A6dK1URrDilQCtQi9JkF3vbU2LcPe~iw4wYYp3VKdwC9aEFuh-eIyZRIZEtGFISE~3SCfQ__&Key-Pair-Id=APKAITJV77WS5ZT7262A"],
            # th.Propert("instructors", th.StringType),      : [                "大森 剛"],
            # th.Propert("requirements", th.StringType),      : {                "list": [                    "このコースでは、実際のケースをもとにワークショップを行います。講師とゲストが「デザイナーチーム」としてケースに挑みますので、受講生のみなさんも、チームの一員になったつもりでご参加ください。",                    "ワークショップの中では、課題やアイデアを１枚の紙にまとめていきます。白い紙とペンを用意してご参加ください。"                ]            },
            # th.Propert("what_you_will_learn", th.StringType),      : {                "list": [                    "実際のケースを例に、「企画を１枚の紙にまとめる力」を磨くことができます。",                    "課題を正しく把握し、状況をシンプルに整理する方法を身につけられます。",                    "企画の「そもそも」を考えるくせを身につけることができます。",                    "企画をまとめる前に、１枚の紙で全体像を把握し、アイデアの検証を行うことができるようになります。"                ]            },
            # th.Propert("images", th.StringType),      : {                "size_48x27": "https://img-c.udemycdn.com/course/48x27/900920_cd28.jpg",                "size_50x50": "https://img-c.udemycdn.com/course/50x50/900920_cd28.jpg",                "size_75x75": "https://img-c.udemycdn.com/course/75x75/900920_cd28.jpg",                "size_96x54": "https://img-c.udemycdn.com/course/96x54/900920_cd28.jpg",                "size_100x100": "https://img-c.udemycdn.com/course/100x100/900920_cd28.jpg",                "size_125_H": "https://img-b.udemycdn.com/course/125_H/900920_cd28.jpg",                "size_200_H": "https://img-c.udemycdn.com/course/200_H/900920_cd28.jpg",                "size_240x135": "https://img-c.udemycdn.com/course/240x135/900920_cd28.jpg",                "size_304x171": "https://img-c.udemycdn.com/course/304x171/900920_cd28.jpg",                "size_480x270": "https://img-c.udemycdn.com/course/480x270/900920_cd28.jpg",                "size_750x422": "https://img-c.udemycdn.com/course/750x422/900920_cd28.jpg"            },
            # th.Propert("mobile_native_deeplink", th.StringType),      : "udemyufb://discover?coursePublishedTitle=triplet_design",
            # th.Propert("locale", th.StringType),      : {              "_class": "locale",              "locale": "ja_JP"          },
            # th.Propert("is_practice_test_course", th.StringType),      : false,
            # th.Propert("primary_category", th.StringType),      : {     "_class": "course_category",     "id": 316,     "title": "Marketing",     "url": "/courses/ufb-marketing/" },
            # th.Propert("primary_subcategory", th.ObjectType([th.Property("")])),      : {     "_class": "course_subcategory",     "id": 458,     "title": "Marketing Strategy",     "url": "/courses/ufb-marketing/ufb-marketing-strategy/" },
            # th.Propert("num_quizzes", th.IntegerType),      : 0,
            # th.Propert("num_practice_tests", th.IntegerType),      : 0,
            # th.Propert("has_closed_caption", th.StringType),      : false,
            # th.Propert("caption_languages", th.StringType),      : [],
            # th.Propert("caption_locales", th.StringType),      : [],
            # th.Propert("estimated_content_length_video", th.IntegerType),      : 178,
            # th.Propert("last_update_date", th.DateTimeType),      : "2016-12-28",
            # th.Propert("xapi_activity_id", th.StringType),      : "https://www.udemy.com/course/900920"
#         },

# from_date = "2021-03-24" will filter

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
