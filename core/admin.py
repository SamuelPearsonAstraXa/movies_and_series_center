from django.contrib import admin
from .models import BannerVideo, TopStory, DidYouKnow, Nationality, Country

admin.site.register(Nationality)
admin.site.register(Country)
admin.site.register(BannerVideo)
admin.site.register(TopStory)
admin.site.register(DidYouKnow)