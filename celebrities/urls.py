from django.urls import path
from . import views

app_name = 'celebrities'

urlpatterns = [
    path('', views.CelebritiesHomeView.as_view(), name='home'),
    path('add/', views.AddCelebrityView.as_view(), name='add'),
    path('create-news/', views.CreateCelebrityNewsView.as_view(), name='create-news'),
]