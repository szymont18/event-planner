from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, reverse
from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views import View
from django.core.exceptions import PermissionDenied
import random
from django.views.generic.edit import FormView
from .forms import *


# Create your views here.

def authenticated(request):
    if request.user.is_authenticated:
        return request.user
    raise PermissionDenied('User is not authenticated')


def proposed_friends(friends):
    distant_friend = []
    random.shuffle(friends)

    for friend in friends[:10]:
        other_friends = friend.friends.all()
        distant_friend.append(random.choice(other_friends))

    all_users = WebsiteUser.objects.all()
    for _ in range(len(distant_friend), 10):
        distant_friend.append(random.choice(all_users))

    return distant_friend


def main_page(request):
    return render(request, 'home/main.html')


def logout_user(request):
    logout(request)
    return redirect('login:login_template')


class FriendsView(View):

    def get(self, request, *args, **kwargs):
        try:
            user = authenticated(request)
        except PermissionDenied:
            return HttpResponseRedirect('login:login_template')

        friends = user.friends.all()

        proposed = proposed_friends(friends)

        extra_content = {'friends': friends,
                         'proposed': proposed}

        return render(request, "home/friends.html", extra_content)

    def post(self, request, *args, **kwargs):
        pass  # TODO: Meet friends. Send them invitation to friends


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'home/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home:profile')

    def form_valid(self, form):
        form.save()
        profile_picture = form.cleaned_data.get('profile_picture')
        if profile_picture:
            self.request.user.profile_picture = profile_picture
            self.request.user.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['instance'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            user = authenticated(self.request)
        except PermissionDenied:
            return context

        profile_form = ProfileForm(instance=user)
        context['form'] = profile_form
        context['picture'] = user.profile_picture

        return context
