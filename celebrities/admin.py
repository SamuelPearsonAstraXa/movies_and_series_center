from django.contrib import admin
from .models import Celebrity, CelebrityNews

admin.site.register(CelebrityNews)
admin.site.register(Celebrity)