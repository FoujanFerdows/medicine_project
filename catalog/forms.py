from django import forms

class ContactForm(forms.Form):
    title       = forms.CharField(max_length=150, label="Title")
    description = forms.CharField(widget=forms.Textarea, label="Description")
    email       = forms.EmailField(label="Email Address")