from django.forms import ModelForm
from .models import *
from django import forms
from .models import Movie, Artist, Rating, Award


class DateInput(forms.DateInput):
    input_type = 'date'


class MovieForm(ModelForm):
    """

    """
    class Meta:
        model = Movie
        fields = '__all__'
        exclude = ['avg_rating', ]
        widgets = {
            'Release_date': DateInput()
        }


class ArtistForm(ModelForm):
    """

    """
    class Meta:
        model = Artist
        fields = '__all__'
        widgets = {
            'dob': DateInput()
        }


class AwardForm(ModelForm):
    """

    """
    class Meta:
        model = Award
        fields = '__all__'
        widgets = {
            'created_at': DateInput()
        }


class RatingForm(ModelForm):
    """

    """
    class Meta:
        model = Rating
        exclude = ['votes', ]
        fields = '__all__'


class SearchForm(ModelForm):
    """

    """
    class Meta:
        model = Movie
        fields = ['name']
