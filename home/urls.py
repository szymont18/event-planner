from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("home-page", views.HomePageView.as_view(), name='home-page'),
    path('invitation/<int:pk>', views.HomePageView.as_view(), name='invitation_response'),
    path('lgout', views.logout_user, name='logout'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('friends/<int:pk>', views.FriendsView.as_view(), name='friends_modification'),
    path('profile', views.ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>', views.UserDetail.as_view(), name="user_detail"),
    path('events', views.EventView.as_view(), name='events'),
    path('events/<slug:event_slug>', views.EventDetailView.as_view(), name="event_detail"),
    path('events/<slug:event_slug>/<int:pk>', views.EventDetailView.as_view(), name='invite_friend'),
]
