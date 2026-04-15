from django.urls import path

from .views import about_page, course_list, lesson_detail, rate_lesson

app_name = "courses"

urlpatterns = [
    path("", course_list, name="list"),
    path("about/", about_page, name="about"),
    path("lesson/<int:lesson_id>/", lesson_detail, name="lesson_detail"),
    path("lesson/<int:lesson_id>/rate/", rate_lesson, name="rate_lesson"),
]
