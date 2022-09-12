from django import forms
from .models import User, UserProfile

class AddUserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ['username']

class AddUserProfileForm(forms.ModelForm):

    class Meta:
        model = UserProfile
        fields = ['speed']