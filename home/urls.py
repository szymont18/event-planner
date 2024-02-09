from django.urls import path
from . import views

app_name = 'home'

urlpatterns = [
    path("home-page", views.main_page, name='home-page'),
    path('lgout', views.logout_user, name='logout'),
    path('friends', views.FriendsView.as_view(), name='friends'),
    path('friends/<int:pk>', views.FriendsView.as_view(), name='friends_modification'),
    path('profile', views.ProfileView.as_view(), name='profile'),
]
