from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView

app_name = 'login'

urlpatterns = [
    path("login", views.LoginTemplate.as_view(), name="login_template"),
    path("sign-up", views.RegisterView.as_view(), name='sign-up'),
    path("password-reset/", views.ResetPasswordView.as_view(), name='password-reset'),
    path('password-change/<uidb64>/<token>/',views.PasswordChangeView.as_view(), name='password-reset-confirm'),
    path("password-reset/sended/", PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),
         name='password-reset-sended'),
    path("password-changed/success", views.password_change_sucess, name='password-change-success')
]