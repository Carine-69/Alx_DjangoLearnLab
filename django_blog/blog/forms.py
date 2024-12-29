from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Comment, Post, Tag
from django.forms import CheckboxSelectMultiple  # Import the widget

# Form for User creation
class CreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

class TagWidget(forms.CheckboxSelectMultiple):
    """
    Custom widget for displaying tags as checkboxes.
    Inheriting from CheckboxSelectMultiple to render a list of checkboxes.
    """
    pass

# Form for Comment creation
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

# Form for Post creation/editing, including tags
class TagForm(forms.ModelForm):
    class Meta:
        model = Post  # Correct 'model' to 'Post'
        fields = ['title', 'content', 'tags']  # Match fields with the Post model

     widgets = {
        'tags': CheckboxSelectMultiple,  # Use CheckboxSelectMultiple for the 'tags' field
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
