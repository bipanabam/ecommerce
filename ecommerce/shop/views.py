from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic

from . import models
# Create your views here.
class CreateProduct(LoginRequiredMixin,generic.CreateView):
    model = models.Product
    fields = ('name','image','description','price','quantity','category')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)

class ListProduct(generic.ListView):
    model = models.Product

class ProductDetail(generic.DetailView):
    model = models.Product
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.increase_view_count()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

class CategoryProduct(generic.TemplateView):
    template_name = "shop/category_product.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product = models.Product.objects.filter(category=self.kwargs.get('pk'))
        context["products"] = product
        return context
    
