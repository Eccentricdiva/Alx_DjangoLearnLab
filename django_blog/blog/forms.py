from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']  # taggit handles tags automatically
        widgets = {
            'tags': forms.TextInput(attrs={'placeholder': 'Add tags separated by commas'}),
        }
