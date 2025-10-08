from django.urls import path
from . import views
from .views import toggle_favourite_ajax
from .views import add_to_cart_ajax

app_name = "shop"

urlpatterns = [
    # Main shop view
    path("", views.main_view, name="main"),

    # Product detail page
    path("product/<slug:slug>/", views.product_detail, name="product_detail"),

    # Cart views
    path("cart/", views.cart_view, name="cart"),
    path("cart/remove/<int:item_id>/", views.remove_from_cart, name="remove_from_cart"),
     path('add-to-cart/<int:product_id>/', add_to_cart_ajax, name='add_to_cart_ajax'),

    # Favourites views
    path("favourites/", views.favourites_view, name="favourites"),
    path('favourites/toggle/<int:product_id>/', views.toggle_favourite_ajax, name='toggle_favourite_ajax'),
    path("favourites/remove/<int:product_id>/", views.remove_from_favourites, name="remove_from_favourites"),
     path("checkout/", views.checkout_view, name="checkout"),
     path("process_checkout/", views.process_checkout, name="process_checkout"),
     path('support/', views.support_view, name='support'),
    
]