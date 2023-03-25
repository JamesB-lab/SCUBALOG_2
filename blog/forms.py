from django import forms
from .models import *

class PostForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'your name'}))
    class Meta:
        model = Post
        fields = "__all__"
        