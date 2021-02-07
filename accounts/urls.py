from django.urls import path, include

from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),

]