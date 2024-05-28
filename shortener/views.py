from django.shortcuts import render, redirect
from .forms import LinkForm
from .models import Link

def index(request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = LinkForm()
	links = Link.objects.all()
	return render(request, 'index.html', {'form': form, 'links': links})