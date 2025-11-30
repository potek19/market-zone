from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Category, Product, Cart, CartItem


def home(request):
    categories = Category.objects.all()
    return render(request, "index.html", {"categories": categories})

def categories(request):
    categories = Category.objects.all()
    return render(request, "categories.html", {"categories": categories})

def products(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products = category.products.all()
    return render(request, "products.html", {"category": category, "products": products})

def trgovina(request):
    categories = Category.objects.all()
    category_id = request.GET.get('category')
    
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = Product.objects.filter(category=selected_category)
    else:
        selected_category = None
        products = Product.objects.all()
    
    return render(request, "trgovina.html", {
        "categories": categories,
        "products": products,
        "selected_category": selected_category,
    })


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

    messages.success(request, f'{product.name} je bil dodan v košarico!')
    return redirect("trgovina")

def cart_view(request):
    cart = _get_cart(request)
    return render(request, "kosarica.html", {"cart": cart})

def update_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    action = request.GET.get('action')
    
    if action == 'increase':
        item.quantity += 1
        item.save()
    elif action == 'decrease':
        if item.quantity > 1:
            item.quantity -= 1
            item.save()
        else:
            item.delete()
    
    return redirect('cart_view')

def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id)
    item.delete()
    return redirect('cart_view')

def checkout_steps(request):
    cart = _get_cart(request)
    
    if request.method == 'POST':
        # Process order (for school project, just show success message)
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        
        # Clear the cart
        cart.items.all().delete()
        
        messages.success(request, f'Hvala {first_name}! Vaše naročilo je bilo uspešno oddano. Potrditev smo poslali na {email}.')
        return redirect('home')
    
    return render(request, "checkout.html", {"cart": cart})


def about(request):
    return render(request, 'o-nas.html')

def services(request):
    return render(request, 'storitev.html')