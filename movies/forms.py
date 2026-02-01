from django import forms
from .models import Movie

class UpdateMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['slug',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }

class UploadMovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['slug',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }