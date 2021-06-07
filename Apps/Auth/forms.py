from django import forms
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput(),required=True)
    class Meta():
        model = User
        fields = ('first_name', 'last_name', 'username','mob','profile_pic', 'password','confirm_password')

