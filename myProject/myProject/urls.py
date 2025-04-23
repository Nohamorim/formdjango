from django.urls import path
from myApp import views

urlpatterns = [
    # rota, view responsável, nome de referência
    # usuarios.com
    path('',views.home,name='home'),
]
