from django import forms
from django.forms import ModelForm
from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile



class CreateUserForm(UserCreationForm):
    
    
    class Meta:
        model=User
        fields= ['username','password1','password2']




class ProfileUpdateForm(ModelForm):
    
    class Meta:
        model=Profile
        fields = ['first_name','email','adress','image']