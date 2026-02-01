from django.urls import path
from . import views

app_name = 'series'

urlpatterns = [
    path('', views.SeriesHomeView.as_view(), name='home'),
    path('upload/', views.UploadSeriesView.as_view(), name='upload'),
    path('latest/', views.LatestSeriesView.as_view(), name='latest'),
    path('upcoming/', views.UpcomingSeriesView.as_view(), name='upcoming'),
    path('<str:slug>/', views.SeriesDetailsView.as_view(), name='details'),
    path('<str:slug>/update/', views.UpdateSeriesView.as_view(), name='update'),
]