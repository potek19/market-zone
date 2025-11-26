from django.shortcuts import render, get_object_or_404, redirect
from .models import Category, Product, Cart, CartItem


def home(request):
    return render(request, "home.html")

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "products.html", {"category": category, "products": products})


# Košarica
def _get_cart(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.create()

    cart, created = Cart.objects.get_or_create(session_key=request.session.session_key)
    return cart

def add_to_cart(request, product_id):
    cart = _get_cart(request)
    product = get_object_or_404(Product, id=product_id)

    item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        item.quantity += 1
    item.save()

    return redirect("cart_view")

def cart_view(request):
    cart = _get_cart(request)
    return render(request, "cart.html", {"cart": cart})

def checkout_steps(request):
    return render(request, "checkout.html")


def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')