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

class DateForm(forms.Form):
    date = forms.DateTimeField(
        input_formats=['%d/%m/%Y %H:%M'],
        widget=forms.DateTimeInput(attrs={
            'class': 'form-control datetimepicker-input',
            'data-target': '#datetimepicker1'
        })
    )

