from django import template

register = template.Library()

@register.filter
def cart_total(cart):
    total = 0
    for item in cart.items.all():
        total += item.product.price * item.quantity
    return total
