from django.shortcuts import render
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from .forms import UploadMovieForm, UpdateMovieForm
from .models import Movie
from django_filters.views import FilterView
from .filters import MovieFilter

class UpcomingMoviesView(FilterView, ListView):
    model = Movie
    template_name = 'movies/upcoming_movies.html'
    paginate_by = 30
    filterset_class = MovieFilter
    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()

        # Showing movies that are to be released in the next 90 days
        upcoming_date = today + timedelta(days=90)

        return Movie.objects.filter(release_date__lte=upcoming_date, release_date__gte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Upcoming Movies'

        return context

class LatestMoviesView(FilterView, ListView):
    model = Movie
    template_name = 'movies/latest_movies.html'
    paginate_by = 30
    filterset_class = MovieFilter
    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()

        cutoff_date = today - timedelta(days=60)

        return Movie.objects.filter(release_date__gte=cutoff_date, release_date__lte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Latest Movies'

        return context

class MovieDetailsView(DetailView):
    model = Movie
    template_name = 'movies/movie_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.object.title
        context['related_movies'] = Movie.objects.filter(category=self.object.category)

        return context

class UpdateMovieView(UpdateView):
    model = Movie
    # fields = '__all__'
    form_class = UpdateMovieForm
    template_name = 'movies/update_movie.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/movies/{self.object.slug}/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Movie'
        return context

class UploadMovieView(CreateView):
    form_class = UploadMovieForm
    template_name = 'movies/upload_movie.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/movies/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload Movie'
        return context

class MoviesHomeView(FilterView, ListView):
    model = Movie
    template_name = 'movies/movies_home.html'
    paginate_by = 30
    filterset_class = MovieFilter

    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()

        return Movie.objects.filter(release_date__lte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        context['title'] = 'Movies'
        context['query_params'] = query_params.urlencode()
        return context