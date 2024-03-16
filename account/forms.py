from django import forms
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser, Otp


class LoginForm(forms.Form):
    phone = forms.CharField(widget=forms.TextInput(attrs={'type':'text', 'placeholder': 'phone or email or username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'type':'password', 'placeholder': 'password'}))
    class Meta:
        model = CustomUser
        fields = ('phone', 'password')

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Full Name'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'type': 'email', 'placeholder': 'Email'}))
    age = forms.CharField(widget=forms.TextInput(attrs={'type': 'number', 'placeholder': 'Age'}))
    username = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Username'}))
    phone = forms.CharField(widget=forms.TextInput(attrs={'type': 'text', 'placeholder': 'Phone'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'type': 'password', 'placeholder': 'Password Again'}))

    class Meta:
        model = CustomUser
        fields = ('full_name', 'email', 'age', 'phone', 'username', 'password1', 'password2')


class CheckOtpForm(forms.ModelForm):
    class Meta:
        model = Otp
        fields = ('verification_code', )
