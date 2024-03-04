# gadgets/urls.py
from django.urls import path
from .views import signup, dashboard, home, login_view, add_product, products, product_list, password_protected_view, add_to_cart, remove_from_cart, view_cart, checkout, order_confirmation, contact_form
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('dashboard/', dashboard, name='dashboard'),
    path('', home, name='home'),
    path('home/', home, name='home'),
    path('products/', products, name='products'),
    path('product_list/', product_list, name='product_list'),
    path('password_protected/', password_protected_view, name='password_protected'),
    path('add_product/', add_product, name='add_product'), 
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('checkout/', checkout, name='checkout'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('view_cart/', view_cart, name='view_cart'),
    path('remove_from_cart/<int:cart_item_id>/', remove_from_cart, name='remove_from_cart'),
    path('order_confirmation/', order_confirmation, name='order_confirmation'),
    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('contact-form/', contact_form, name='contact_form'),
]
