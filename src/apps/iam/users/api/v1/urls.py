# Third Party Stuff
from django.urls import path

from . import views

urlpatterns = [
    path("", views.UserCreateView.as_view()),
    path("login/", views.LoginView.as_view()),
    path("<uuid:pk>/", views.UserDetailView.as_view()),
]
