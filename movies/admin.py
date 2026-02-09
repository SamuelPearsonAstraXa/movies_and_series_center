from django.contrib import admin
from .models import Movie, MovieReview

admin.site.register(MovieReview)
admin.site.register(Movie)