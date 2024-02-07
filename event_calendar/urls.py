from django.urls import path
from . import views

app_name = 'event_calendar'

urlpatterns = [
    path("home-page", views.main_page, name='home-page'),
    path('lgout', views.logout_user, name='logout')
]
