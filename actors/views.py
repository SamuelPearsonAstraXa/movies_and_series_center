from django.shortcuts import render
from django.views.generic import ListView, TemplateView

class ActorsHomeView(TemplateView):
    template_name = 'actors/actors_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Actors'

        return context