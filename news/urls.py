from django.urls import path
from . import views

app_name = 'news'

urlpatterns = [
    path('', views.NewsHomeView.as_view(), name='home'),
    path('add/', views.AddNewsView.as_view(), name='add'),
]