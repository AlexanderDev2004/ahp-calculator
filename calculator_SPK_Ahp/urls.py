from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Halaman utama
    path('about/', views.about, name='about'),  # Halaman About
]
