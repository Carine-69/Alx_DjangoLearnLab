from django.db.models import Q
from .models import comment
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.models import User
from .models import post, tag

class CreationForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model=User
		fields = ('username','email','password1','password2')

class CommentForm(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['content']

class tagForm(forms.ModelForm):
	class Meta:
		method = Post
		fields = ['title','contents', 'tags']
	tags = forms.ModelMultipleChoiceField(querySet=tag.objects.all(), required=False)



	def save(self, commit=True):
    		post = super().save(commit=False)
    		post.save()

    	# Add tags to the post
    		tags = self.cleaned_data['tags']
    		for tag in tags:
        		post.tags.add(tag)
    
    		return post
	
def search(request):
    query = request.GET.get('q', '')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) | 
            Q(content__icontains=query) | 
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.all()
    return render(request, 'blog/templates/blog/search_results.html', {'posts': posts, 'query': query})
