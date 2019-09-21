from django import forms
from django.forms import widgets


class ReviewForm(forms.Form):
    name = forms.CharField(max_length=100, required=True, label='Name')
    email = forms.EmailField(required=True, label='Email')
    text = forms.CharField(max_length=1000, required=True, label='Text', widget=widgets.Textarea)


