from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import post
from django.contrib import render, redirect
from .form import registration
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
    template_name = 'blog/post_delete.html'
    success_url = reverse_lazy('post_list')  # Redirect to the post list page after deletion

	def test_func(self):
    post = self.get_object()
    return self.request.user == post.author  # Only allow the author to delete the post

