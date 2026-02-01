from django.db import models
from uuid import uuid4
from django.utils.text import slugify
from PIL import Image
from accounts.models import CustomUser

class Country(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    code = models.CharField(max_length=5)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

class Nationality(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.name}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name)
        
        super().save(*args, **kwargs)

class AcademicQualification(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    reward_name = models.CharField(max_length=200)
    reward_code = models.CharField(max_length=200, blank=True, default='')
    reward_abbreviation = models.CharField(max_length=200)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.reward_name}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.reward_abbreviation)

        super().save(*args, **kwargs)

class DidYouKnow(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    text = models.TextField()
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.text[:50]}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)

        super().save(*args, **kwargs)

class TopStory(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField(max_length=10000)
    banner_img = models.ImageField(upload_to='top_stories/banner_images')
    upload_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.id}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)

        super().save(*args, **kwargs)

class BannerVideo(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=500)
    video = models.FileField(upload_to='banner_videos')
    upload_date = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.id}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)

        super().save(*args, **kwargs)