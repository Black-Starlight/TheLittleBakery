from django.contrib.auth.models import User
from django import forms
from django.contrib.auth.models import User
from .models import Comments, Profile, ProfileComments, Recipes


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['comment']

class addRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipes
        fields = ('title','caption','imageDir','bakeType','serve','prepTime','cookTime','kcal','fat','carbs','sugar','protein','salt','ingredients','recipe')


class ProfileCommentsForm(forms.ModelForm):

    class Meta:
        model = ProfileComments
        fields = ['comment']
