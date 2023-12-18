from django.views.generic import TemplateView
from shop.models import Product, Category

class HomePage(TemplateView):
    template_name = 'base/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = Product.objects.all()
        context["product_most_search"] = Product.objects.filter(view_count__isnull=False).order_by('-view_count')
        context["categories"] = Category.objects.all()
        return context
    

class ThanksPage(TemplateView):
    template_name = 'base/thanks.html'

