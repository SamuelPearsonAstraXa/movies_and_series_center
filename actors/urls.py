from django.urls import path
from . import views

app_name = 'actors'

urlpatterns = [
    path('', views.ActorsHomeView.as_view(), name='actors-home'),
]