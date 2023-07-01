from django import forms
from django.forms import widgets

from guest_book.models import GuestBook


class GuestBookForm(forms.ModelForm):
    class Meta:
        model = GuestBook
        fields = ['guest_name', 'guest_email', 'text_records']
        widgets = {'guest_name': widgets.TextInput(attrs={'class': 'form-control'}),
                   'guest_email': widgets.EmailInput(attrs={'class': 'form-control'}),
                   'text_records': widgets.Textarea(attrs={'class': 'form-control', 'rows': 2})}
