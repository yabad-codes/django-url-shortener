from django.shortcuts import render, redirect, get_object_or_404
from .forms import LinkForm
from .models import Link
from .base62 import base62_decode

def index(request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			link = form.save(commit=False)
			if request.user.is_authenticated:
				link.user = request.user
			link.save()
			return redirect('index')
	else:
		form = LinkForm()
	links = Link.objects.all().order_by('created_at')
	return render(request, 'index.html', {'form': form, 'links': links})

def redirect_view(request, short_code):
	link_id = base62_decode(short_code)
	link = get_object_or_404(Link, pk=link_id)
	link.views_count += 1
	link.save()
	return redirect(link.url)