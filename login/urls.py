from django.urls import path
from . import views

urlpatterns = [
    path("login", views.LoginTemplate.as_view(), name="login_template"),
    path("success/", views.success, name="home-page"),
    path("sign-up", views.RegisterView.as_view(), name='sign-up')
]