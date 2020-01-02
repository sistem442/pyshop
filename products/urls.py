from django.urls import path
from . import views

app_name = 'products'
urlpatterns = [
    path('<str:category>/', views.products_index),
    path('', views.products_index),
    path('new', views.new),
]
