from django.shortcuts import render, redirect
from .forms import SignupForm, LoginForm
from django.contrib.auth import login, authenticate, logout

def index(request):
	return render(request, 'index.html')

def user_signup(request):
	if request.method == 'POST':
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('login')
	else:
		if request.user.is_authenticated:
			return redirect('home')
		form = SignupForm()
	return render(request, 'signup.html', {'form': form})

def user_login(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(request, username=username, password=password)
			if user:
				login(request, user)
				return redirect('home')
	else:
		if request.user.is_authenticated:
			return redirect('home')
		form = LoginForm()
	return render(request, 'login.html', {'form': form})

def user_logout(request):
	logout(request)
	return redirect('index')