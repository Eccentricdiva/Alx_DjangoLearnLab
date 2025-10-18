from django import forms
from .models import Post, Comment

# ✅ Form for creating/updating Posts
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

# ✅ Form for creating/updating Comments
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
