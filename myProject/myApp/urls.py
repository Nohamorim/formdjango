from . import views
from django.urls import path

urlpatterns = [
    path('manual/', views.form_manual, name="form_manual"),
    path('formdjango/', views.form_django, name="form_django"),
    path('modelform/', views.form_modelform, name="form_modelform"),
]