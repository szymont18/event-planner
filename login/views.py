from django.shortcuts import render
from django.contrib.auth.views import LoginView, FormView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse, reverse_lazy
from .forms import MyAuthenticationForm, RegisterForm, ResetPasswordForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class LoginTemplate(LoginView):
    template_name = 'login/login.html'
    redirect_authenticated_user = True
    authentication_form = MyAuthenticationForm

    extra_context = {
        "authentication_form": MyAuthenticationForm()
    }

    def get_success_url(self):
        return reverse_lazy("home:home-page")


class RegisterView(FormView):
    template_name = 'login/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy("login:login_template")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'login/reset_password.html'
    email_template_name = 'login/reset_email.html'
    subject_template_name = 'login/reset_email_subject'
    success_url = 'sended'
    form_class = ResetPasswordForm


class PasswordChangeView(PasswordResetConfirmView):
    template_name = 'login/password_change.html'
    success_url = reverse_lazy('login: password-change-success')
    form_class = ChangePasswordForm


def password_change_sucess(request):
    return render(request, 'login/password_change_success.html')
