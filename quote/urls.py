from django.urls import path
from . import views

app_name = 'quote'

urlpatterns = [
    path('', views.home, name='home'),
    path('success/', views.success, name='success'),
    path('quote/', views.quote, name='quote'),
    path('shopping/', views.shopping, name='shopping'),
    path('about/', views.about, name='about'),
]