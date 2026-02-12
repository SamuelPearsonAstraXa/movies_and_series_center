from django.db import models
from django.utils.text import slugify
from PIL import Image
from uuid import uuid4
from io import BytesIO
from django.core.files.base import ContentFile
from django.utils import timezone

class News(models.Model):
    STATUS_CHOICES = [('draft','Draft'), ('published', 'Published')]
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=50000)
    featured_img = models.ImageField(upload_to='news/featured_imgs/%d/%m/%y')
    tags = models.CharField(max_length=1000)
    author = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateField(default=timezone.datetime.today, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES)
    slug = models.SlugField(default='', blank=True)
    
    def __str__(self):
        return f'{self.title}'
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.id)

        if self.featured_img:
            img = Image.open(self.featured_img)

            # Resizing
            img.thumbnail((500,500))

            buffer = BytesIO()
            img.save(buffer, format='JPEG', quality=100)
            buffer.seek(0)

            self.featured_img = ContentFile(buffer.read(), name=self.featured_img.name)

        super().save(*args, **kwargs)