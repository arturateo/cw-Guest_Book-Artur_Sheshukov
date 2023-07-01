from django import forms
from django.forms import widgets


class SearchForm(forms.Form):
    search = forms.CharField(max_length=100, required=False,
                                widget=forms.TextInput(attrs={"class": "form-control", "placeholder": 'Поиск по книге'}))


