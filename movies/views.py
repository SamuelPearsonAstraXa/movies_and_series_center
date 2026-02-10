from django.shortcuts import render
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from django.views.generic import TemplateView, CreateView, ListView, DetailView, UpdateView
from .forms import UploadMovieForm, UpdateMovieForm, AddMovieReviewForm
from .models import Movie, MovieReview
from django.db.models import Q
# from django_filters.views import FilterView
# from .filters import MovieFilter

class AddMovieReviewView(CreateView):
    form_class = AddMovieReviewForm
    template_name = 'movies/add_movie_review.html'

    def form_valid(self, form):
        movie = Movie.objects.get(id=self.request.POST.get('movie-id'))
        review = form.save(commit=False)

        review.movie = movie
        review.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/movies/{movie.slug}/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add Movie Review'
        return context

class UpcomingMoviesView(ListView):
    model = Movie
    template_name = 'movies/upcoming_movies.html'
    paginate_by = 30
    # filterset_class = MovieFilter
    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()

        # Showing movies that are to be released in the next 90 days
        upcoming_date = today + timedelta(days=90)
        queryset = Movie.objects.filter(release_date__lte=upcoming_date, release_date__gte=today)
        movie_q = str(self.request.GET.get('upcoming_movie_query', '')).strip()
        
        if movie_q:
            queryset = queryset.filter(
                Q(title__icontains=movie_q) | Q(description__icontains=movie_q) | Q(category__icontains=movie_q) |
                Q(production_year__icontains=movie_q) | Q(production_country__icontains=movie_q) | Q(producer__icontains=movie_q) | 
                Q(director__icontains=movie_q)
                )
        
        return queryset.order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Upcoming Movies'

        return context

class LatestMoviesView(ListView):
    model = Movie
    template_name = 'movies/latest_movies.html'
    paginate_by = 30
    # filterset_class = MovieFilter
    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()

        cutoff_date = today - timedelta(days=60)
        queryset = Movie.objects.filter(release_date__gte=cutoff_date, release_date__lte=today)
        movie_q = str(self.request.GET.get('latest_movie_query', '')).strip()
        
        if movie_q:
            queryset = queryset.filter(
                Q(title__icontains=movie_q) | Q(description__icontains=movie_q) | Q(category__icontains=movie_q) |
                Q(production_year__icontains=movie_q) | Q(production_country__icontains=movie_q) | Q(producer__icontains=movie_q) | 
                Q(director__icontains=movie_q)
                )
        
        return queryset.order_by('-upload_date')

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
        context['review_form'] = AddMovieReviewForm
        context['reviews'] = MovieReview.objects.filter(movie=self.object)

        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        if 'submit_review' in request.POST:
            form = AddMovieReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.reviewer = self.request.user
                review.movie = self.object
                review.save()

                return JsonResponse({'success':True})
            else:
                return JsonResponse({'success':False, 'errors':form.errors})
        else:
            return JsonResponse({'success': False, 'error':'Unknown form submission.'})

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

class MoviesHomeView(ListView):
    model = Movie
    template_name = 'movies/movies_home.html'
    paginate_by = 30
    # filterset_class = MovieFilter

    context_object_name = 'movies'

    def get_queryset(self):
        today = timezone.now().date()
        queryset = Movie.objects.filter(release_date__lte=today)
        
        movie_q = str(self.request.GET.get('movie_query', '')).strip()
        
        if movie_q:
            queryset = queryset.filter(
                Q(title__icontains=movie_q) | Q(description__icontains=movie_q) | Q(category__icontains=movie_q) |
                Q(production_year__icontains=movie_q) | Q(production_country__icontains=movie_q) | Q(producer__icontains=movie_q) | 
                Q(director__icontains=movie_q)
                )
        
        return queryset.order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        context['title'] = 'Movies'
        context['query_params'] = query_params.urlencode()
        return context