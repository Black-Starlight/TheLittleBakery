from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    #favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))

    class Meta:
        model = Comment
        fields = ('name', 'rate', 'text')
