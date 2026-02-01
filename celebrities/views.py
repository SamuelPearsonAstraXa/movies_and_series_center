from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, CreateView
from .models import CelebrityNews
from .forms import AddCelebrityForm, CreateCelebrityNewsForm

class CreateCelebrityNewsView(CreateView):
    form_class = CreateCelebrityNewsForm
    template_name = 'celebrities/create_celebrity_news.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/celebrities/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Create celebrity news'

        return context
    
class AddCelebrityView(CreateView):
    form_class = AddCelebrityForm
    template_name = 'celebrities/add_celebrity.html'

    def form_valid(self, form):
        form.save()
        
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':True, 'success_url': f'/celebrities/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success':False, 'error': form.errors}, status=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Add a celebrity'

        return context

class CelebritiesHomeView(ListView):
    model = CelebrityNews
    template_name = 'celebrities/celebrities_home.html'
    context_object_name = 'celebrity_news'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['title'] = 'Celebrities'

        return context