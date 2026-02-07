from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import TemplateView, ListView, CreateView, DetailView, UpdateView
from django.utils import timezone
from datetime import timedelta
# from django_filters.views import FilterView
from .forms import UploadSeriesForm, UpdateSeriesForm
from .models import Series

class SeriesDetailsView(DetailView):
    model = Series
    template_name = 'series/series_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.object.title
        context['related_series'] = Series.objects.filter(category=self.object.category)

        return context

class UpdateSeriesView(UpdateView):
    model = Series
    # fields = '__all__'
    form_class = UpdateSeriesForm
    template_name = 'series/update_series.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/series/{self.object.slug}/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Update Series'
        return context

class UpcomingSeriesView(ListView):
    model = Series
    template_name = 'series/upcoming_series.html'
    paginate_by = 30
    # filterset_class = SeriesFilter
    context_object_name = 'series'
    filterset_fields = ['title']

    def get_queryset(self):
        today = timezone.now().date()

        # Showing series that are to be released in the next 90 days
        upcoming_date = today + timedelta(days=90)

        return Series.objects.filter(release_date__lte=upcoming_date, release_date__gte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Upcoming series'

        return context

class LatestSeriesView(ListView):
    model = Series
    template_name = 'series/latest_series.html'
    paginate_by = 30
    # filterset_class = SeriesFilter
    context_object_name = 'series'
    filterset_fields = ['title']

    def get_queryset(self):
        today = timezone.now().date()

        cutoff_date = today - timedelta(days=60)

        return Series.objects.filter(release_date__gte=cutoff_date, release_date__lte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Latest series'

        return context

class UploadSeriesView(CreateView):
    form_class = UploadSeriesForm
    template_name = 'series/upload_series.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/series/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Upload Series'
        return context

class SeriesHomeView(ListView):
    template_name = 'series/series_home.html'
    model = Series
    paginate_by = 30
    context_object_name = 'series'
    filterset_fields = ['title']

    def get_queryset(self):
        today = timezone.now().date()

        return Series.objects.filter(release_date__lte=today).order_by('-upload_date')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        query_params = self.request.GET.copy()
        if 'page' in query_params:
            query_params.pop('page')

        context['title'] = 'Series'
        context['query_params'] = query_params.urlencode()

        return context