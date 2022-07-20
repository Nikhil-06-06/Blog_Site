from dataclasses import field
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile 

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:                                                      #gives us a nested nameSpace for configuration, keeps the configurations in one place its says as follows 
        model = User                                                 #this is the model to be affected, means whenever we do form.save() the data will be saved in this model/table in database
        fields = ['username', 'email', 'password1', 'password2']     #specifies the fields that we want to have in the form and in what order

class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']