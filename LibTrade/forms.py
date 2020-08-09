from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from accounts.models import User

class SignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = User
        fields = ['username', 'email']
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        return user
