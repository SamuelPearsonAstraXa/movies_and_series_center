from django import forms
from .models import Movie, MovieReview

class AddMovieReviewForm(forms.ModelForm):
    class Meta:
        model = MovieReview
        fields = ['text',]

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