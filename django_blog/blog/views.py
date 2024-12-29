from django.contrib.auth.decorators import login_required
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
\            comment = form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form, 'post': post})

# View for editing a comment
class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ['content']
    template_name = 'blog/comment_form.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can edit their comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

# View for deleting a comment
class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'blog/comment_confirm_delete.html'

    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author  # Only the author can delete their comment

    def get_success_url(self):
        return reverse_lazy('post_detail', kwargs={'pk': self.object.post.pk})

