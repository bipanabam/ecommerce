from .models import Cart

def cart_item_count(request):
    if request.user.is_authenticated:
        cart = Cart.objects.filter(user=request.user)
        cart_item_count = cart.count()
    else:
        cart_item_count = 0
    return {'cart_item_count': cart_item_count}