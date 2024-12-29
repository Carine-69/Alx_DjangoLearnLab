from django import forms
from .models import Post, Tag
from django.forms import CheckboxSelectMultiple

# Step 1: Define a custom TagWidget class
class TagWidget(CheckboxSelectMultiple):
    """
    Custom widget for displaying tags as checkboxes.
    Inheriting from CheckboxSelectMultiple to render a list of checkboxes.
    """
    pass  # We can extend this further if we need additional customization.

# Step 2: Define the form for Post creation/editing, including tags
class TagForm(forms.ModelForm):
    class Meta:
        model = Post  # Correct 'model' to 'Post'
        fields = ['title', 'content', 'tags']  # Match fields with the Post model

        # Step 3: Use the widgets dictionary for custom widget handling
        widgets = {
            'tags': TagWidget()  # Use our custom TagWidget for rendering tags as checkboxes
        }

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        required=False
    )

    def save(self, commit=True):
        post = super().save(commit=False)  # Save post object first
        post.save()  # Save the post to the database

        # Add the tags to the post
        tags = self.cleaned_data['tags']
        for tag in tags:
            post.tags.add(tag)  # Associate each selected tag with the post

        return post

