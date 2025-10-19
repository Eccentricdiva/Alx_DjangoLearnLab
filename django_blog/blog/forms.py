from django import forms
from .models import Post, Tag


class PostForm(forms.ModelForm):
    # Custom field for entering tags as a comma-separated string
    tags = forms.CharField(
        required=False,
        help_text="Enter tags separated by commas (e.g. python, django, api)"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

    def save(self, commit=True):
        # Save the Post instance first
        instance = super().save(commit=False)

        if commit:
            instance.save()

            # Process tags
            tag_names = self.cleaned_data['tags']
            if tag_names:
                tag_list = [t.strip() for t in tag_names.split(',') if t.strip()]
                for name in tag_list:
                    tag, created = Tag.objects.get_or_create(name=name)
                    instance.tags.add(tag)

        return instance
