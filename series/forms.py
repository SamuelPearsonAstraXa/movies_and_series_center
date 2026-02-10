from django import forms
from .models import Series, SeriesReview

class AddSeriesReviewForm(forms.ModelForm):
    class Meta:
        model = SeriesReview
        fields = ['text',]

class UpdateSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
        exclude = ['slug',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }

class UploadSeriesForm(forms.ModelForm):
    class Meta:
        model = Series
        fields = '__all__'
        exclude = ['slug',]

        widgets = {
            'release_date': forms.DateInput(attrs={'type':'date'}),
        }