from django.shortcuts import render
from django.utils import timezone
from datetime import timedelta
from django.views.generic import TemplateView
from .models import BannerVideo, TopStory, DidYouKnow
from movies.models import Movie
from series.models import Series

class HomeView(TemplateView):
    template_name = 'core/index.html'

    banner_videos = BannerVideo.objects.all()
    top_stories = TopStory.objects.all()
    did_you_knows = DidYouKnow.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # Current day
        today = timezone.now().date()

        # 2 months backward
        cutoff_date = today - timedelta(days=60)

        # month forward
        upcoming_date = today + timedelta(days=90)

        context['banner_video'] = self.banner_videos[0]
        context['top_stories'] = self.top_stories
        context['top_story'] = self.top_stories[0]
        context['did_you_know'] = self.did_you_knows[0]
        context['tagline'] = 'Find your joy through movies and series.'
        context['latest_movies'] = Movie.objects.filter(release_date__gte=cutoff_date, release_date__lte=today).order_by('-upload_date')
        context['upcoming_movies'] = Movie.objects.filter(release_date__lte=upcoming_date, release_date__gte=today).order_by('-upload_date')
        context['latest_series'] = Series.objects.filter(release_date__gte=cutoff_date, release_date__lte=today).order_by('-upload_date')
        context['upcoming_series'] = Series.objects.filter(release_date__lte=upcoming_date, release_date__gte=today).order_by('-upload_date')

        return context