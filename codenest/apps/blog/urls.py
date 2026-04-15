from django.urls import path

from .views import blog_list, like_post

app_name = "blog"

urlpatterns = [
    path("", blog_list, name="list"),
    path("<int:post_id>/like/", like_post, name="like"),
]
