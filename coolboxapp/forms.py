from django import forms
from .models import User
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView
from django.db.models import fields

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name']