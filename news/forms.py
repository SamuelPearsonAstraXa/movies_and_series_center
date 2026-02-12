from django import forms
from .models import News

class AddNewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'
        exclude = ['slug',]