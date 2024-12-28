from djnago.contrib import render, redirect
from .form import registration
from django.contrib import messages

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
