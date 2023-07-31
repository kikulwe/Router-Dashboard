from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.router_dashboard, name='router_dashboard'),
    # Add other URL patterns as needed...
]