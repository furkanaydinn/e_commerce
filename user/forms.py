from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django import forms


class SignUpForm(UserCreationForm):
    username = forms.CharField(max_length=30, widget = forms.TextInput(attrs={'class':'user-input','placeholder':'Kullanıcı adı'}))
    email = forms.EmailField(max_length=200, widget = forms.EmailInput(attrs = {'class':'user-input','placeholder':'Mail adresi'}))
    password1 = forms.CharField(max_length=16, widget=forms.PasswordInput(attrs = {'class':'user-input','placeholder':'Parola'}))
    password2 = forms.CharField(max_length=16, widget = forms.PasswordInput(attrs = {'class':'user-input','placeholder':'Parola Tekrarı'}))

    class Meta:
        model = User
        fields = ["username","email","password1","password2"]

        