from django.shortcuts import render
from django.contrib.auth.views import LoginView, FormView, PasswordResetView
from django.urls import reverse, reverse_lazy
from .forms import MyAuthenticationForm, RegisterForm, ResetPasswordForm
from django.http import HttpResponseRedirect
from django.contrib.messages.views import SuccessMessageMixin


# Create your views here.


class LoginTemplate(LoginView):
    template_name = 'login/login.html'
    # redirect_authenticated_user = True
    authentication_form = MyAuthenticationForm

    extra_context = {
        "authentication_form": MyAuthenticationForm()
    }

    def get_success_url(self):
        return reverse("home-page")


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
    success_url = reverse_lazy("password-reset-done")
    form_class = ResetPasswordForm


def success(request):
    return render(request, 'login/success_tmp.html')


def failure(request):
    return render(request, 'login/failure_tmp.html')
