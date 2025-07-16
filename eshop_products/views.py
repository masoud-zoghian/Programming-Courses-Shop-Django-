from unicodedata import category
from django.http import Http404
from django.shortcuts import render
from django.views.generic.list import ListView
from eshop_products.models import Product, ProductGallery
from eshop_tag.models import Tag
from eshop_products_category.models import ProductCategory
from eshop_order.forms import UserNewOrderForm


# Create your views here.
class ProductsList(ListView):
    template_name = 'products_list.html'
    paginate_by = 5

    def get_queryset(self):
        return Product.objects.get_active_products()

def product_detail(request, *args, **kwargs):
    get_product_id = kwargs['product_id']
    new_order_form = UserNewOrderForm(request.POST or None, initial=({'product_id':get_product_id}))
    title = kwargs['title']

    product = Product.objects.get_product_by_id(get_product_id)
    if product is None:
        raise Http404('محصول مورد نظر یافت نشد!')

    gallery = ProductGallery.objects.filter(product_id=get_product_id)
    # print(gallery)

    related_products = Product.objects.get_queryset().filter(categories__product=product).distinct()
    print(related_products)

    product.visits += 1
    product.save()
    
    featured_products = Product.objects.filter(featured=True)


    context = {
        'product':product,
        'gallery':gallery,
        'related_products':related_products,
        'new_order_form':new_order_form,
        'featured_products':featured_products,
        
    }
    tag = Tag.objects.first()
    # print(tag)
    # print(tag.products.all())
    # print(product.tag_set.all())

    return  render(request, 'product_detail.html', context)

class SearchProducts(ListView):
    template_name = 'products_list.html'
    paginate_by = 10

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query is not None:
            return Product.objects.search_products(query)
        return Product.objects.get_active_products()

class ProductsListByCategory(ListView):
    template_name = 'products_list.html'
    paginate_by = 6

    def get_queryset(self):
        category_name = self.kwargs['category_name']
        print(category_name)
        categories = ProductCategory.objects.filter(name__iexact=category_name)
        if categories is None:
            raise Http404('صفحه مورد نظر یافت نشد!')
        return Product.objects.get_product_by_category(category_name)

def products_categories_partial(request):
    categories = ProductCategory.objects.all()
    context = {
        'categories':categories
    }
    return render(request,'categories_view_partial.html', context)