from django.db import models
from django.utils.text import slugify
from uuid import uuid4
from PIL import Image

class Movie(models.Model):
    id = models.UUIDField(default=uuid4, editable=False, primary_key=True)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    banner_img = models.ImageField(upload_to='movies/banner_images')
    trailer = models.FileField(upload_to='movies/trailers')
    production_year = models.PositiveIntegerField()
    production_country = models.TextField(default='', blank=True)
    category = models.CharField(help_text='eg. Comedy, or Horror', max_length=100, default='', blank=True)
    duration = models.CharField(default='', blank=True)
    producer = models.CharField(max_length=200, default='', blank=True)
    director = models.CharField(max_length=200, default='', blank=True)
    release_date = models.DateField(null=True, blank=True)
    upload_date = models.DateField(auto_now_add=True)
    upload_time = models.TimeField(auto_now_add=True)
    is_latest = models.BooleanField(default=False)
    is_trending = models.BooleanField(default=False)
    is_upcoming = models.BooleanField(default=False)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.title} ({self.production_year})'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title + str(self.production_year) + str(self.id))

        super().save(*args, **kwargs)