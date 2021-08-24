from django import forms
from idmpapp.models import Rating, RATING_CHOICE


# GENDER_CHOICES = (
#     (1, ('Male')),
#     (2, ('Female')),
# )
# class searchForm:

#     box = forms.ModelMultipleChoiceField(
#         choices=GENDER_CHOICES,
#         widget=forms.CheckboxSelectMultiple(),
#         label='Search',
#     )


class Ratingform(forms.ModelForm):
    description = forms.CharField(widget=forms.Textarea(
        attrs={'class': 'materialize-textarea'}), required=False)
    rate = forms.ChoiceField(choices=RATING_CHOICE,
                             widget=forms.Select(), required=True)

    class Meta:
        model = Rating
        fields = ('text', 'rate')
