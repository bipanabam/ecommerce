from django.shortcuts import render, get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import Http404
from django.views import generic

from authentication.models import CustomUser

from .models import Cart, Order

from shop.models import Product

from .forms import OrderForm

# Create your views here.

#Cart
@login_required
def add_to_cart(request,product_id):
    product = get_object_or_404(Product,pk=product_id)

    try:
        existing_item = Cart.objects.get(product=product, user=request.user)
        existing_item.product = product
        existing_item.product_quantity += 1
        existing_item.user = request.user
        existing_item.save()
    except Cart.DoesNotExist:
        new_item = Cart.objects.create(product=product,user=request.user, product_quantity=1)
        new_item.save()
    return redirect('cart:view_cart')

class CartView(LoginRequiredMixin,generic.ListView):
    model = Cart
    template_name = "orders/view_cart.html"
    context_object_name = 'cart'

class CartItemDelete(LoginRequiredMixin,generic.DeleteView):
    model = Cart
    success_url = reverse_lazy('cart:view_cart')

    def get(self, request, *args, **kwargs):
      return self.delete(request, *args, **kwargs)



#Order
@login_required
def place_order(request):
    cart = get_object_or_404(Cart,user=request.user)

    total = cart.product.price * cart.product_quantity

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            new_order = form.save(commit=False)
            new_order.cart = cart
            new_order.user = request.user
            new_order.total = total
            new_order.save()
            return redirect("cart:order_user")
    else:
        form = OrderForm()
    return render(request,'orders/order_form.html',{'form':form, 'total':total})

class UserOrderList(LoginRequiredMixin,generic.ListView):
    model = Order
    template_name = 'orders/user_order.html'
    context_object_name = 'order_list'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(user=self.request.user)
        return context
    
class OrderDetail(LoginRequiredMixin,generic.DetailView):
    model = Order

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["orders"] = Order.objects.filter(user=self.request.user)
        return context

    



    
    
