from django.urls import path
from .views import home, redirect_view, stats_view

urlpatterns = [
	path('home/', home, name='home'),
	path('home/v/<str:short_code>/', redirect_view, name='redirect_view'),
	path('stats/<str:short_code>/', stats_view, name='stats_view'),
]