from django.db import models
import os
import random
from django.db.models import Q
from eshop_products_category.models import ProductCategory


def get_file_extension(file):
    base_name = os.path.basename(file)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image(instance, filename):
    rand_name = random.randint(1,9999999999)
    name , ext = get_file_extension(filename)
    final_name = f"{instance.id}-{instance.title}-{rand_name}{ext}"
    return f"products/{final_name}"

class ProductManager(models.Manager):
    def get_active_products(self):
        return self.get_queryset().filter(active=True)

    def get_product_by_id(self, product_id):
        qs = self.get_queryset().filter(id=product_id, active=True)
        if qs.count() == 1:
            return qs.first()
        else:
            return None

    def search_products(self, query):
        lookup = (Q(title__icontains=query) | Q(description__icontains=query) |
                  Q(tag__title__icontains=query))
        return self.get_queryset().filter(lookup, active=True).distinct()

    def get_product_by_category(self, category_name):
        return self.get_queryset().filter(categories__name__iexact=category_name)

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=150, verbose_name='عنوان')
    description = models.TextField(verbose_name='توضیحات')
    price = models.DecimalField(decimal_places=2, max_digits=15, verbose_name ='قیمت')
    image = models.ImageField(upload_to=upload_image,null=True,blank=True,verbose_name='تصویر')
    active = models.BooleanField(default=False, verbose_name='فعال/غیرفعال')
    time = models.DateTimeField(auto_now_add=True)
    categories = models.ManyToManyField(ProductCategory, blank=True, verbose_name='دسته بندی')
    featured = models.BooleanField(default=False, verbose_name='محصول ویژه')
    visits = models.IntegerField(default=0, verbose_name='تعداد مشاهده')
    publisher_name = models.CharField(max_length=255, null=True, blank=True, verbose_name="نام ناشر")
    course_duration = models.CharField(max_length=155, null=True, blank=True, verbose_name="مدت زمان دوره")

    objects = ProductManager()

    class Meta:
        verbose_name = 'محصول'
        verbose_name_plural = 'محصولات'

    def __str__(self):
        return self.title
    def get_product_detail_url(self):
        return f"/products/{self.id}/{self.title.replace(' ' , '-')}"

def upload_image_gallery(instance, filename):
    rand_name = random.randint(1,9999999999)
    name , ext = get_file_extension(filename)
    final_name = f"{instance.id}-{instance.title}-{rand_name}{ext}"
    return f"gallery/{final_name}"


class ProductGallery(models.Model):
    title = models.CharField(max_length=100, verbose_name='عنوان')
    image = models.ImageField(upload_to=upload_image_gallery,null=True,blank=True,verbose_name='تصویر')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='انتخاب محصول')

    class Meta:
        verbose_name = 'تصویر'
        verbose_name_plural = ' گالری تصاویر'

    def __str__(self):
        return self.title