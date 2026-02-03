from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('register/', views.RegisterView.as_view(), name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('<str:slug>/edit/', views.EditUserProfileView.as_view(), name='edit-user-profile'),
    path('<str:slug>/', views.UserProfileView.as_view(), name='user-profile'),
]