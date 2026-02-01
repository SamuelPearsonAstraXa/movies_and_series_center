from django.db import models
from accounts.models import CustomUser
from django.utils.text import slugify
from uuid import uuid4

class Episode(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    series = models.ForeignKey('Series', on_delete=models.CASCADE, related_name='episode_series')
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    upload_date = models.DateTimeField(auto_now_add=True)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    production_year = models.PositiveIntegerField()
    production_countries = models.TextField(default='')
    episode_number = models.PositiveIntegerField(default=1)
    director = models.CharField(max_length=200, default='')
    trailer = models.FileField(null=True, upload_to='series/episodes/trailers')
    banner_img = models.ImageField(upload_to='series/episodes/banner_images', null=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title + str(self.id))
        super().save(*args, **kwargs)

class Series(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    uploaded_by = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    episodes = models.ManyToManyField(Episode, blank=True, related_name='series_episodes')
    release_date = models.DateField(null=True, blank=True)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    director = models.CharField(default='', blank=True, max_length=200)
    category = models.CharField(max_length=200, default='', blank=True)
    producer = models.CharField(default='', blank=True, max_length=200)
    banner_img = models.ImageField(upload_to='series/banner_images', null=True)
    trailer = models.FileField(upload_to='series/trailers', null=True)
    production_year = models.PositiveIntegerField()
    production_countries = models.TextField(default='', blank=True)
    num_of_episodes = models.PositiveIntegerField(default=1, blank=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.id}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.title + str(self.id))
        
        super().save(*args, **kwargs)