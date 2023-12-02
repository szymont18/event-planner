from django.urls import path
from . import views
from django.contrib.auth.views import PasswordResetDoneView, PasswordResetConfirmView

urlpatterns = [
    path("login", views.LoginTemplate.as_view(), name="login_template"),
    path("home", views.success, name="home-page"),
    path("sign-up", views.RegisterView.as_view(), name='sign-up'),
    path("password-reset/", views.ResetPasswordView.as_view(), name='password-reset'),
    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='login/password_reset_confirm.html'), #TODO: Create View in views
         name='password_reset_confirm'),
    path("password_reset/done/", PasswordResetDoneView.as_view(template_name='login/password_reset_done.html'),
         name='password-reset-done')
]