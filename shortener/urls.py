from django.urls import path
from .views import index, redirect_view

urlpatterns = [
	path('', index, name='index'),
	path('view/<str:short_code>/', redirect_view, name='redirect'),
]