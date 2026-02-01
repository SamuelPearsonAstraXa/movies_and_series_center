from django.db import models
from uuid import uuid4
from core.models import Nationality, AcademicQualification
from movies.models import Movie
from django.utils.text import slugify

class Actor(models.Model):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    birth_date = models.DateField(blank=True, null=True)
    occupation = models.CharField(max_length=200)
    featured_movies = models.ManyToManyField(Movie, blank=True)
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