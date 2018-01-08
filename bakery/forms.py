from django.contrib.auth.models import User
from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ('name', 'rate', 'text')
        
class UserForm(forms.ModelForm):
    password = forms.Charfield(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password']

