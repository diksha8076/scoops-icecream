from django.urls import path
from . import views

urlpatterns =[
    path('', views.home, name='home'),
    path('flavors/', views.flavors, name='flavors'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('add-to-cart/<str:flavor_name>/', views.add_to_cart, name='add_to_cart'),
    path('cart/', views.cart_view, name='cart'),
    path('remove/<str:flavor_name>/', views.remove_from_cart, name='remove_from_cart'),
    path('checkout/', views.checkout, name='checkout'),
]
