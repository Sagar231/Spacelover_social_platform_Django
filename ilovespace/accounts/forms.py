from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
# from django.contrib.auth import get_user_model


class UserCreateForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    #     self.fields['username'].label = "Dispaly Name"
    #     self.fields['email'].label = "Email Address"
        