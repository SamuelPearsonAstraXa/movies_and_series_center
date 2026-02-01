from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.views.generic import CreateView, DetailView
from movies.models import Movie
from series.models import Series, Episode
from core.models import DidYouKnow, TopStory
from celebrities.models import Celebrity
from actors.models import Actor

from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm

class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'accounts/profile.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = self.object.get_full_name
        context['series'] = Series.objects.all()
        context['actors'] = Actor.objects.all()
        context['celebrities'] = Celebrity.objects.all()
        context['movies'] = Movie.objects.all()
        context['did_you_knows'] = DidYouKnow.objects.all()
        context['top_stories'] = TopStory.objects.all()

        return context

def logout_view(request):
    logout(request)
    return redirect('core:home')

class RegisterView(CreateView):
    form_class = CustomUserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')