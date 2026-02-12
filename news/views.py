from django.shortcuts import render
from django.http import JsonResponse
from .models import News
from .forms import AddNewsForm
from django.views.generic import ListView, TemplateView, DetailView, CreateView

class AddNewsView(CreateView):
    form_class = AddNewsForm
    template_name = 'news/add_news.html'

    def form_valid(self, form):
        form.save()

        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': True, 'success_url':f'/'})
        return super().form_valid(form)

    def form_invalid(self, form):
        if self.request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'success': False, 'errors':form.errors}, staus=400)
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add news'
        return context

class NewsHomeView(ListView):
    paginate_by = 50
    model = News
    template_name = 'news/news_home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'News Updates'
        return context