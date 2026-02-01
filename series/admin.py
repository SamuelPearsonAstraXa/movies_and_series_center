from django.contrib import admin
from .models import Series, Episode

admin.site.register(Episode)
admin.site.register(Series)