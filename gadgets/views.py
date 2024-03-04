# gadgets/views.py

from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from .forms import SignUpForm, ProductForm, AddProductForm, PasswordForm, CheckoutForm
from .models import Page, Product, Cart, CartItem, Order, OrderItem
from .forms import ContactForm

# Custom Product Page View
def custom_product_page(request):
    # Your view logic here
    return render(request, 'custom_product_page.html')

# Signup View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Dashboard View
@login_required(login_url='/login/')
def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products': products})

# Add Product View
def add_product(request):
    if request.method == 'POST':
        form = AddProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Product added successfully!')
            return redirect('products')  # Redirect to the products page
    else:
        form = AddProductForm()

    return render(request, 'add_product.html', {'form': form})

# Product List View
def product_list(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Home View
def home(request):
    products = Product.objects.all()
    return render(request, 'home.html', {'products': products})

# Login View
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('home')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Products View
def products(request):
    products = Product.objects.all()
    return render(request, 'products.html', {'products': products})

# Password Protected View
def password_protected_view(request):
    if request.method == 'POST':
        form = PasswordForm(request.POST)
        if form.is_valid():
            entered_password = form.cleaned_data['password']
            stored_password = '*wk2dnh^57mwus9'

            if entered_password == stored_password:
                return redirect('add_product')
            else:
                form.add_error('password', 'Incorrect password. Try again.')

    else:
        form = PasswordForm()

    return render(request, 'password_protected.html', {'form': form})

# Admin View
def admin_view(request):
    return render(request, 'add_product.html')

# Add to Cart View
@login_required
def add_to_cart(request, product_id):
    # Retrieve the product
    product = get_object_or_404(Product, id=product_id)

    # Get or create the user's cart
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Check if the product is already in the cart
    cart_item, item_created = CartItem.objects.get_or_create(cart=cart, product=product)

    if not item_created:
        # If the product is already in the cart, increase the quantity
        cart_item.quantity += 1
        cart_item.save()

    return redirect('products')

# View Cart View
def view_cart(request):
    # Retrieve the user's cart and related items
    user_cart = get_object_or_404(Cart, user=request.user)
    user_cart_items = user_cart.cartitem_set.all()

    # Calculate total bill
    total_bill = sum(item.product.price for item in user_cart_items)

    return render(request, 'view_cart.html', {'cart_items': user_cart_items, 'total_bill': total_bill})


# Checkout View
def checkout(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Create an Order instance
            order = Order.objects.create(
                user=request.user,
                address=form.cleaned_data['address'],
                city=form.cleaned_data['city'],
                state=form.cleaned_data['state'],
                zip_code=form.cleaned_data['zip_code'],
                phone_number=form.cleaned_data['phone_number'],
                country=form.cleaned_data['country'],
                total_price=0.0  # You need to adjust this based on your logic
            )

            # Retrieve the user's cart items
            user_cart_items = CartItem.objects.filter(cart__user=request.user)

            # Update the order's total_price based on the cart items
            order.total_price = sum(item.total_price for item in user_cart_items)
            order.save()

            # Create OrderItem instances and link them to the order
            product_names = []  # To store the product names

            for cart_item in user_cart_items:
                order_item = OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    total_price=cart_item.total_price
                )

                # Add the product name to the list
                product_names.append(cart_item.product.name)

            # Save the product names as a comma-separated string in the order
            order.products = ', '.join(product_names)
            order.save()

            # Clear the user's cart
            user_cart_items.delete()

            # Redirect or do further processing
            return redirect('order_confirmation')  # Redirect to order confirmation page

    else:
        form = CheckoutForm()

    # Retrieve the user's cart and related items
    user_cart = get_object_or_404(Cart, user=request.user)
    user_cart_items = user_cart.cartitem_set.all()

    # Calculate total bill
    total_bill = sum(item.total_price for item in user_cart_items)

    return render(request, 'checkout.html', {'form': form, 'cart_items': user_cart_items, 'total_bill': total_bill})


@login_required(login_url='/login/')
def order_confirmation(request):
    # Get the last order for the current user
    order = Order.objects.filter(user=request.user).order_by('-created_at').first()

    # Ensure that order is not None before proceeding
    if order:
        # Retrieve the order items
        order_items = OrderItem.objects.filter(order=order)
        
        # Calculate the total bill
        total_bill = sum(item.total_price for item in order_items)

        # Pass the order, order_items, and total_bill to the template
        return render(request, 'order_confirmation.html', {'order': order, 'order_items': order_items, 'total_bill': total_bill})
    else:
        # Handle the case where no order is found
        return render(request, 'order_confirmation.html', {'order': None, 'order_items': None, 'total_bill': None})

# Get Last Order Utility Function
def get_last_order(user):
    # Get the last order for the user or return None if no orders
    return Order.objects.filter(user=user).order_by('-created_at').first()

# Get Cart Items Utility Function
def get_cart_items(user):
    return CartItem.objects.filter(cart__user=user)

# Remove from Cart View
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id)
    cart_item.delete()
    return redirect('view_cart')

def contact_form(request):
    return render(request, 'contact_form.html')