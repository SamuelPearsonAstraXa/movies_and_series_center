from django.contrib import admin
from .models import Movie, Review

admin.site.register(Review)
admin.site.register(Movie)