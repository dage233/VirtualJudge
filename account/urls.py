from django.urls import path
from account.views import LogoutAPI, LoginAPI, RegisterAPI, ProfileAPI

urlpatterns = [
    path("login/", LoginAPI.as_view(), name="login"),
    path("logout/", LogoutAPI.as_view(), name="logout"),
    path("register/", RegisterAPI.as_view(), name="register"),
    path('profile/', ProfileAPI.as_view(), name='profile'),
]
