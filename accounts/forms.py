from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django.forms.utils import ValidationError

from accounts.models import Book, Trade


class BookCreateForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['name', 'author', 'image', 'tags']
