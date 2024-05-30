from django.shortcuts import render, redirect, get_object_or_404
from .forms import LinkForm
from .models import Link, Click
from .base62 import base62_decode
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_protect
from django.utils import timezone
from datetime import timedelta
from django.http import JsonResponse, HttpResponseForbidden
from django.db import IntegrityError
from django.contrib import messages

@login_required(login_url='/login/')
def home(request):
	if request.method == 'POST':
		form = LinkForm(request.POST)
		if form.is_valid():
			try:
				link = form.save(commit=False)
				link.user = request.user
				link.save()
				return redirect('home')
			except IntegrityError as e:
				messages.error(request, 'This link already exists.')
	else:
		form = LinkForm()
	links = Link.objects.filter(user=request.user).order_by('created_at')
	return render(request, 'home.html', {'form': form, 'links': links})

def redirect_view(request, short_code):
	link_id = base62_decode(short_code)
	link = get_object_or_404(Link, pk=link_id)
	link.views_count += 1
	link.save()
	Click.objects.create(link=link)
	return redirect(link.url)

@login_required(login_url='/login/')
def stats_view(request, short_code):
	link_id = base62_decode(short_code)
	link = get_object_or_404(Link, pk=link_id)

	labels = [(timezone.now() - timedelta(days=i)).strftime("%b %d") for i in range(30, -1, -1)]
	labels.reverse()

	values = [0] * 31

	last_30_days = timezone.now() - timedelta(days=30)
	clicks = Click.objects.filter(link=link, clicked_at__gte=last_30_days)

	for click in clicks:
		day_index = (timezone.now() - click.clicked_at).days
		values[30 - day_index] += 1
	
	data = {
		"labels": labels,
		"values": values
	}
	return render(request, 'stats.html', {'short_code': short_code, 'link': link, 'data': data})

@csrf_protect
@login_required(login_url='/login/')
def delete_link(request, short_code):
	link = get_object_or_404(Link, short_code=short_code)
	if link.user != request.user:
		return HttpResponseForbidden("You are not authorized to delete this link.")
	link.delete()
	return redirect('home')