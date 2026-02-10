from django.contrib import admin
from .models import Series, Episode, SeriesReview

admin.site.register(SeriesReview)
admin.site.register(Episode)
admin.site.register(Series)