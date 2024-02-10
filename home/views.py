from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse_lazy, reverse
from django.utils import timezone
from django.views import View
from django.core.exceptions import PermissionDenied
import random
from django.views.generic.edit import FormView
from .forms import *
from django.contrib.auth.decorators import login_required


# Create your views here.

def authenticated(request):
    if request.user.is_authenticated:
        return request.user
    raise PermissionDenied('User is not authenticated')


def proposed_friends(friends):
    distant_friend = []
    rnd_shuffle = [i for i in range(len(friends))]
    random.shuffle(rnd_shuffle)

    for friend_ind in rnd_shuffle:
        friend = friends[friend_ind]
        other_friends = friend.friends.all()
        distant_friend.append(random.choice(other_friends))

    all_users = WebsiteUser.objects.all()
    for _ in range(len(distant_friend), 10):
        distant_friend.append(random.choice(all_users))

    return distant_friend


@login_required
def main_page(request):
    return render(request, 'home/main.html')


def logout_user(request):
    logout(request)
    return redirect('login:login_template')


class FriendsView(LoginRequiredMixin, View):
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
        action_type = request.POST.get('type')
        user = authenticated(request)
        friend = WebsiteUser.objects.get(pk=kwargs['pk'])
        if action_type == 'unfollow':
            self.unfollow(user, friend)

        elif action_type == 'follow':
            self.follow(user, friend)

        return HttpResponseRedirect(reverse('home:friends'))

    def follow(self, user: WebsiteUser, friend: WebsiteUser):
        user.friends.add(friend)

    def unfollow(self, user: WebsiteUser, friend: WebsiteUser):
        user.friends.remove(friend)


class ProfileView(LoginRequiredMixin, FormView):
    template_name = 'home/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('home:profile')

    def form_valid(self, form):
        form.save()
        profile_picture = self.request.FILES['picture']
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


class EventView(LoginRequiredMixin, FormView):
    template_name = 'home/events.html'
    form_class = EventForm
    success_url = reverse_lazy('home:events')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        user = authenticated(self.request)

        events = user.events.all()
        events = events.filter(date__gt=timezone.now()).order_by('date')

        context['events'] = events
        return context

    def form_valid(self, form):
        event = form.save(commit=False)
        event.organizer = self.request.user
        event.save()

        return super().form_valid(form)


