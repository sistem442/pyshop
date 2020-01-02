from django.urls import path
from . import views

urlpatterns = [
    path('index', views.products_index),
    path('new', views.new),
]
