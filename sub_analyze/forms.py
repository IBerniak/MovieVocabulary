from django import forms
from .models import Movie

class SearchingForm(forms.ModelForm):

    class Meta:
        model = Movie
        fields = ('title', 'year',)
