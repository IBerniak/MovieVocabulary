from django import forms
from .models import SearchingRequest

class SearchingForm(forms.ModelForm):

    class Meta:
        model = SearchingRequest
        fields = ('title', 'year',)
