from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.MoviesHomeView.as_view(), name='home'),
    path('latest/', views.LatestMoviesView.as_view(), name='latest'),
    path('upcoming/', views.UpcomingMoviesView.as_view(), name='upcoming'),
    path('upload/', views.UploadMovieView.as_view(), name='upload'),
    path('<str:slug>/', views.MovieDetailsView.as_view(), name='movie-details'),
    path('<str:slug>/update/', views.UpdateMovieView.as_view(), name='update-movie'),
]