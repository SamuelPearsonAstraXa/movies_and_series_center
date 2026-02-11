from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView, TemplateView, CreateView
from django.db.models import Q
from .models import CelebrityNews, Celebrity
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
    model = Celebrity
    template_name = 'celebrities/celebrities_home.html'
    context_object_name = 'celebrities'
    paginate_by = 50
    
    def get_queryset(self):
        queryset = super().get_queryset()
        celebrities_q = str(self.request.GET.get('search_query', '')).strip()
        
        if celebrities_q:
            queryset = queryset.filter(
                Q(name__icontains=celebrities_q) | Q(occupation__icontains=celebrities_q) | Q(biography__icontains=celebrities_q) |
                Q(religion__icontains=celebrities_q) | Q(academic_history__icontains=celebrities_q) | Q(home_town__icontains=celebrities_q)
                )
        
        return queryset.order_by('name')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        celebrities_q = str(self.request.GET.get('search_query', '')).strip()
        if not celebrities_q:
            context['banner_celebrity'] = Celebrity.objects.all()[0]
        context['title'] = 'Celebrities'

        return context