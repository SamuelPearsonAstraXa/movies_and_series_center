from django.db import models
from django.utils.text import slugify
from accounts.models import CustomUser
from core.models import AcademicQualification, Nationality
from uuid import uuid4

class CelebrityNews(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    celebrity = models.ForeignKey('Celebrity', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    news_text = models.TextField(max_length=10000)
    author = models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    upload_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'News about {self.celebrity.name}'

    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)

        super().save(*args, **kwargs)

class Celebrity(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=200)
    biography = models.TextField(max_length=10000)
    religion = models.CharField(max_length=200, blank=True, default='')
    academic_history = models.TextField(max_length=5000)
    academic_qualifications = models.ManyToManyField(AcademicQualification, blank=True)
    home_town = models.CharField(max_length=100)
    nationality = models.ForeignKey(Nationality, on_delete=models.DO_NOTHING)
    slug = models.SlugField(default='', blank=True)

    def __str__(self):
        return f'{self.name}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.name + str(self.id))

        super().save(*args, **kwargs)