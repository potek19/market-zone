from .models import Cart

def cart_context(request):
    """Add cart information to all templates"""
    session_key = request.session.session_key
    if session_key:
        try:
            cart = Cart.objects.get(session_key=session_key)
            cart_count = sum(item.quantity for item in cart.items.all())
        except Cart.DoesNotExist:
            cart_count = 0
    else:
        cart_count = 0
    
    return {
        'cart_count': cart_count
    }
