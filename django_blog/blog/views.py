from django.contrib.auth.decorators import login_required
from djnago.db.models import Q
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import post, comment
from django.contrib import render, redirect
from .forms import registration, commentForm
from django.contrib import messages
from .forms import postform
from django.urls import reverse_lazy

def registration(request):
	if request.method == 'POST':
		form = UserRegistrtionForm(request.POST)
		if form.is_valid():
			form.save()
			messages.sucess(request,'Your account has been created! you can now login.')
			return redirect('login')
	else:
		form = UserRegistrationForm()
	return render(request, 'blog/templates/registation.html',{'form':form})

def profile(request):
	if request.method == 'POST',
		form = UserRegistrationForm(requst.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect('profile')
	else:
		form = UserRegistration(instance=request.user)
	return render(request, 'blog/templates/profile.html',{'form':form})


class postListView(ListView):
	model = post
	name = 'blog/templates/blog/ListView.html'
	context_object_name = 'posts'

class DetailView():
	model = post
	template_name = 'blog/templates/blog/post_detail.html'
	context_object_name = 'post'

class postCreateView(LoginRequiredMixin, CreateView): 
	model = post
	form_class = postform
	template_name = 'blog/templates/blog/CreateView.html'
	success_url = reverse_lazy('ListView') # after successful creaton, it redirects to list view

	def form_valid(self, form):
		from.instance.author = self.request.user # this assign the logged in user as the author of the post
		return super().form_valid(form)

class postUpdateView(LoginRequiredMixin, UserPassesMixin, UpdateView):
	method = post
	form_class = postform
	template_name = 'blog/templates/blog/updateView.html'
	
	def test_func(self):
	post = self.get.object()
	return self.request.user == post.author # only author of post can edit it


	def get_success_url(self):
	return reverse_lazy('post_detail', kwaegs={'pk': self.object.pk})

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/templates/blog/post_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list page after deletion

	def test_func(self):
    post = self.get_object()
    return self.request.user == post.author  # Only allow the author to delete the post

@login_required
def CommentCreateView(request, post_id):
    post = Post.objects.get(id=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/templates/blog/add_comment.html', {'form': form, 'post': post})

# View for editing a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/templates/blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can edit their comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

# View for deleting a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/templates/blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can delete their comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

    def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()
    return render(request, 'blog/templates/blog/posts_by_tag.html', {'posts': posts, 'tag': tag})

   def search(request):
    query = request.GET.get('q', '')  # Get the search query from the URL
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |  # Search in the title
            Q(content__icontains=query) |  # Search in the content
            Q(tags__name__icontains=query)  # Search in the tag name
        ).distinct()  # Ensure no duplicates in the result
    else:
        posts = Post.objects.all()  # If no query, return all posts

    return render(request, 'blog/templates/blog/search_results.html', {'posts': posts, 'query': query})

# View for displaying posts by tag
def posts_by_tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    posts = tag.posts.all()  # Get all posts associated with this tag
    return render(request, 'blog/templates/blog/posts_by_tag.html', {'posts': posts, 'tag': tag})
