from django.urls import path
from . import views

urlpatterns = [
    path("", views.LoginTemplate.as_view(), name="login_template"),
    path("success/", views.success, name="success")
]