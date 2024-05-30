from django.shortcuts import render, redirect, get_object_or_404
from .forms import LinkForm
from .models import Link
from .base62 import base62_decode
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login/')
def home(request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			link = form.save(commit=False)
			link.user = request.user
			link.save()
			return redirect('home')
	else:
		form = LinkForm()
	links = Link.objects.filter(user=request.user).order_by('created_at')
	return render(request, 'home.html', {'form': form, 'links': links})

def redirect_view(request, short_code):
	link_id = base62_decode(short_code)
	link = get_object_or_404(Link, pk=link_id)
	link.views_count += 1
	link.save()
	return redirect(link.url)