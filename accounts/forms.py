from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser
from django import forms

class EditUserProfileForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

        exclude = ['is_staff', 'email', 'is_superuser', 'groups', 'last_login', 'date_joined', 'user_permissions', 'slug', 'is_active', 'password']
        # ['last_login', 'is_staff', 'is_superuser', 'groups', 'is_active', 'date_joined', 'user_permissions', 'slug','password']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
        }

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = '__all__'
        # exclude = ['last_login', 'is_staff', 'is_superuser', 'groups', 'is_active', 'date_joined', 'user_permissions', 'slug','password']

        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type':'date'}),
        }

class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = '__all__'