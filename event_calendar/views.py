from django.shortcuts import render, redirect
from django.contrib.auth import logout


# Create your views here.

def main_page(request):
    return render(request, 'event_planner/main.html')


def logout_user(request):
    logout(request)
    return redirect('login_template')
