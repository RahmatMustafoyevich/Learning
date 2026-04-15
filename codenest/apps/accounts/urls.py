from django.contrib.auth.views import LogoutView
from django.urls import path

from .views import UserLoginView, profile, signup

app_name = "accounts"

urlpatterns = [
    path("login/", UserLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("signup/", signup, name="signup"),
    path("profile/", profile, name="profile"),
]
