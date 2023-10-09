from django import forms
from django.contrib.auth.models import User

from .models import Profile

class UserForm(forms.ModelForm):
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control stylish-input',
    }))

    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput(attrs={
        'class': 'form-control stylish-input',
    }))
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'form-control stylish-input',}),

            'email': forms.EmailInput(attrs={'class': 'form-control stylish-input',})
        }

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'phone']
        widgets = {
            'image': forms.ClearableFileInput(attrs={'class': 'form-control stylish-file',}),
            'phone': forms.TextInput(attrs={'class': 'form-control stylish-input',}),
        }
        
            