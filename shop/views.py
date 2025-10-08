from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, Category, CartItem, Favourite
from .forms import FilterForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render
from .models import Product, Category
from django.db import models
from .forms import CheckoutForm
from .models import CartItem, OrderItem, Order
from django.contrib import messages
from .forms import SupportMessageForm
from .models import SupportMessage
from django.http import JsonResponse
from django.views.decorators.http import require_POST


def main_view(request):
    # Get filters from URL
    category_slug = request.GET.get('category')
    price_range = request.GET.get('price')
    query = request.GET.get('q')

    # Start with all products
    products = Product.objects.all()

    # Category filter
    if category_slug:
        products = products.filter(category__slug=category_slug)

    # Price filter
    if price_range:
        if price_range == "0-50":
            products = products.filter(price__lt=50)
        elif price_range == "50-100":
            products = products.filter(price__gte=50, price__lt=100)
        elif price_range == "100-200":
            products = products.filter(price__gte=100, price__lt=200)
        elif price_range == "200+":
            products = products.filter(price__gte=200)

    # Search filter
    if query:
        products = products.filter(name__icontains=query)

    # Categories for dropdown
    categories = Category.objects.all()

    # Get user's favourite product IDs
    user_favourite_ids = []
    if request.user.is_authenticated:
        user_favourite_ids = Favourite.objects.filter(user=request.user).values_list('product_id', flat=True)

    return render(request, 'shop/main.html', {
        'products': products,
        'categories': categories,
        'user_favourite_ids': list(user_favourite_ids)
    })



def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug)
    return render(request, "shop/product_card.html", {"product": product})



@login_required
def add_to_cart_ajax(request, product_id):
    if request.user.is_authenticated:
        product = get_object_or_404(Product, id=product_id)
        cart_item, created = CartItem.objects.get_or_create(user=request.user, product=product)
        if not created:
            cart_item.quantity += 1
            cart_item.save()
        total_items = CartItem.objects.filter(user=request.user).count()
        return JsonResponse({'status': 'success', 'total_items': total_items})
    return JsonResponse({'status': 'error', 'message': 'User not authenticated'})

@login_required
def cart_view(request):
    items = CartItem.objects.filter(user=request.user).select_related('product')
    total = sum([item.subtotal() for item in items])
    return render(request, "shop/cart.html", {"items": items, "total": total})

@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, pk=item_id, user=request.user)
    item.delete()
    return redirect("shop:cart")

@login_required
def toggle_favourite_ajax(request, product_id):
    if request.user.is_authenticated:
        product = Product.objects.get(id=product_id)
        fav, created = Favourite.objects.get_or_create(user=request.user, product=product)
        if not created:
            fav.delete()
            return JsonResponse({'status': 'removed'})
        return JsonResponse({'status': 'added'})
    return JsonResponse({'status': 'error'})

@login_required
def favourites_view(request):
    favs = Favourite.objects.filter(user=request.user).select_related('product')
    return render(request, "shop/favourites.html", {"favs": favs})


def main(request):
    products = Product.objects.all()
    return render(request, 'shop/main.html', {'products': products})

@login_required
@require_POST
def add_to_favourites(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    if product in user.favourites.all():
        user.favourites.remove(product)
        status = 'removed'
    else:
        user.favourites.add(product)
        status = 'added'
    return JsonResponse({'status': status})

@login_required
def remove_from_favourites(request, product_id):
    """Remove a product from the user's favourites."""
    product = get_object_or_404(Product, id=product_id)
    Favourite.objects.filter(user=request.user, product=product).delete()
    return redirect('shop:favourites')

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("shop:main") 
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {"form": form})


@login_required
def checkout_view(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in items)

    if not items:
        return redirect('shop:cart')

    form = CheckoutForm()
    return render(request, 'shop/checkout.html', {'form': form, 'items': items, 'total': total})


@login_required
def process_checkout(request):
    items = CartItem.objects.filter(user=request.user)
    total = sum(item.subtotal() for item in items)

    if request.method == 'POST' and items:
        form = CheckoutForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total
            order.save()

            # Save order items
            for item in items:
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.product.price
                )
                # Optionally reduce stock:
                item.product.inventory -= item.quantity
                item.product.save()

            # Clear the user's cart
            items.delete()

            return render(request, 'shop/order_success.html', {'order': order})
    else:
        form = CheckoutForm()

    return redirect('shop:checkout')

@login_required
def support_view(request):
    if request.method == 'POST':
        form = SupportMessageForm(request.POST)
        if form.is_valid():
            support_msg = form.save(commit=False)
            support_msg.user = request.user
            support_msg.save()
            messages.success(request, "Your message has been sent to support!")
            form = SupportMessageForm()
    else:
        form = SupportMessageForm()

    user_messages = SupportMessage.objects.filter(user=request.user).order_by('-created_at')

    return render(request, 'shop/support.html', {
        'form': form,
        'user_messages': user_messages
    })

@login_required
@require_POST
def add_to_favourites(request, product_id):
    product = Product.objects.get(id=product_id)
    user = request.user
    if product in user.favourites.all():
        user.favourites.remove(product)
        status = 'removed'
    else:
        user.favourites.add(product)
        status = 'added'
    return JsonResponse({'status': status})