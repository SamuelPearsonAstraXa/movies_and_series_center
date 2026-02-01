from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
from PIL import Image
from django.utils.text import slugify

from .managers import CustomUserManager

class CustomUser(AbstractUser):
    id = models.UUIDField(default=uuid4, primary_key=True, editable=False)
    email = models.EmailField(_('email address'), unique=True)
    profile_img = models.ImageField(upload_to='profile_images/', default='profile_images/avatar.png', blank=True)
    slug = models.SlugField(default='', blank=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    date_of_birth = models.DateField(blank=True, null=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
    def save(self, *args, **kwargs):
        if self.slug == '':
            self.slug = slugify(self.username)

        super().save(*args, **kwargs)
        if self.profile_img:
            img = Image.open(self.profile_img.path)
            if img.width > 300 or img.height > 300:
                img.thumbnail((300,300))
                img.save(self.profile_img.path)