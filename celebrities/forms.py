from django import forms
from .models import Celebrity, CelebrityNews

class CreateCelebrityNewsForm(forms.ModelForm):
    class Meta:
        model = CelebrityNews
        fields = '__all__'
        exclude = ['slug',]

class AddCelebrityForm(forms.ModelForm):
    class Meta:
        model = Celebrity
        fields = '__all__'
        exclude = ['slug',]

        widgets = {
            'birth_date': forms.DateInput(attrs={'type':'date'})
        }