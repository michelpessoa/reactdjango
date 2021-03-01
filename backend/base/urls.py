from django.urls import path
from . import views


urlpatterns = [
    path('', views.getRoutes, name='routes'),
    path('products/', views.getProdutcs, name='products'),
    path('products/<str:pk>/', views.getProdutc, name='product'),
]