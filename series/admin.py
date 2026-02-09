from django.contrib import admin
from .models import Series, Episode, Review

admin.site.register(Review)
admin.site.register(Episode)
admin.site.register(Series)