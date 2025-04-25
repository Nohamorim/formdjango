from . import views
from django.urls import path

urlpatterns = [
    path('', views.home, name='home'),
    path('usuarios/', views.listagem_usuarios, name='listagem_usuarios'),
    ]