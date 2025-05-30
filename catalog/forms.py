from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

from django import forms

class ContactForm(forms.Form):
    title = forms.CharField(
        max_length=150,
        label="Title",
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter a subject...',
            'class': 'form-control'
        })
    )

    description = forms.CharField(
        label="Description",
        widget=forms.Textarea(attrs={
            'placeholder': 'Write your message...',
            'class': 'form-control',
            'rows': 5
        })
    )

    email = forms.EmailField(
        label="Email Address",
        widget=forms.EmailInput(attrs={
            'placeholder': 'you@example.com',
            'class': 'form-control'
        })
    )


class SignUpForm(UserCreationForm):
    first_name    = forms.CharField(max_length=30, required=True, label="First Name")
    last_name     = forms.CharField(max_length=30, required=True, label="Last Name")
    email         = forms.EmailField(required=True, label="Email")
    health_status = forms.CharField(
        widget=forms.Textarea(attrs={'rows':3}),
        required=False,
        label="Current Health Status"
    )

    class Meta:
        model  = User
        fields = ['username', 'first_name', 'last_name', 'email', 'health_status', 'password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name  = self.cleaned_data['last_name']
        user.email      = self.cleaned_data['email']
        if commit:
            user.save()           
        return user

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model  = User
        fields = ['first_name', 'last_name', 'email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model  = Profile
        fields = ['health_status']
        widgets = {
            'health_status': forms.Textarea(attrs={'rows':4}),
        }
  
