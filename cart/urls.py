from django.urls import path
from . import views


urlpatterns = [
    path('CartDetails/', views.cart_details, name='CartDetails'),
    path('AddCart/<int:product_id>/', views.add_cart, name='AddCart'),
    path('Decrement/<int:product_id>/', views.min, name='Decrement'),
    path('Delete/<int:product_id>/', views.Delete, name='Delete'),


]