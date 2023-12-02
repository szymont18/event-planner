from django.shortcuts import render
from django.contrib.auth.views import LoginView, FormView, PasswordResetView, PasswordResetConfirmView
from django.urls import reverse, reverse_lazy
from .forms import MyAuthenticationForm, RegisterForm, ResetPasswordForm, ChangePasswordForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class LoginTemplate(LoginView):
    template_name = 'login/login.html'
    authentication_form = MyAuthenticationForm
    success_url = reverse_lazy('home-page')
    extra_context = {
        "authentication_form": MyAuthenticationForm()
    }

    def get_success_url(self):  # TODO: Check if it is necessary
        return reverse("home-page")

    def form_invalid(self, form):
        context = {'errors': 'Incorrect Username or Password. Note that both fields may be case-sensitive',
                   'authentication_form': form}

        return render(self.request, self.template_name, context)


class RegisterView(FormView):
    template_name = 'login/registration.html'
    form_class = RegisterForm
    success_url = reverse_lazy("home-page")

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class ResetPasswordView(SuccessMessageMixin, PasswordResetView):
    template_name = 'login/reset_password.html'
    email_template_name = 'login/reset_email.html'
    subject_template_name = 'login/reset_email_subject'
    success_url = reverse_lazy("password-reset-sended")
    form_class = ResetPasswordForm


class PasswordChangeView(PasswordResetConfirmView):
    template_name = 'login/password_change.html'
    success_url = reverse_lazy('password-change-success')
    form_class = ChangePasswordForm


def password_change_sucess(request):
    return render(request, 'login/password_change_success.html')


def success(request):
    return render(request, 'login/success_tmp.html')


def failure(request):
    return render(request, 'login/failure_tmp.html')
