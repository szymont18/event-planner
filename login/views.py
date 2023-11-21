from django.shortcuts import render
from django.contrib.auth.views import LoginView, FormView
from django.urls import reverse
from .forms import MyAuthenticationForm, RegisterForm
from django.http import HttpResponseRedirect


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
    success_url = 'success/'

    def form_valid(self, form):
        print("Success")
        form.save()
        return super().form_valid(form)


def success(request):
    return render(request, 'login/success_tmp.html')


def failure(request):
    return render(request, 'login/failure_tmp.html')
