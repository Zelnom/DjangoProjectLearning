from django.urls import path

from userextend import views

urlpatterns = [
    path("sign_up/", views.UserCreateView.as_view(), name="sign-up")
]
