from django.contrib import admin
from eshop_products.models import Product, ProductGallery

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['__str__','title','price','active','featured']

    class Meta:
        model = Product
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductGallery)