from django import forms
from videoteca.models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
