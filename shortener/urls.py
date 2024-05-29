from django.urls import path
from .views import home, redirect_view

urlpatterns = [
	path('home/', home, name='home'),
	path('home/v/<str:short_code>/', redirect_view, name='redirect_view'),
]