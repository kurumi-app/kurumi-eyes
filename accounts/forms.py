from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import *


class CreateUserForm(UserCreationForm):
    invite = forms.CharField(max_length=12, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'invite']

    def clean_invite(self):
        invite = self.cleaned_data.get("invite")
        if not Invites.objects.filter(invite=invite).exists():
            raise forms.ValidationError("Invalid invite code")
        return invite



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["bio", "avatar"]