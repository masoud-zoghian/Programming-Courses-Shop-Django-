from django.db import models
import os
import random
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

def get_file_extension(file):
    base_name = os.path.basename(file)
    name , ext = os.path.splitext(base_name)
    return name , ext

def upload_image(instance, filename):
    rand_name = random.randint(1,9999999999)
    name , ext = get_file_extension(filename)
    final_name = f"{rand_name}{ext}"
    return f"setting/{final_name}"

# Create your models here.
class Settings(models.Model):
    email = models.EmailField(verbose_name="ایمیل شرکت")
    phone = models.CharField(max_length=200, verbose_name='تلفن تماس')
    mobile = models.CharField(max_length=150, verbose_name='شماره همراه')
    fax = models.CharField(max_length=150, verbose_name='شماره فکس')
    adress = models.CharField(max_length=250, verbose_name='آدرس')
    copy_right = models.CharField(max_length=250, verbose_name='متن کپی رایت')
    about = models.TextField(verbose_name='متن درباره ما')
    instagram = models.CharField(max_length=250, verbose_name='آدرس صفحه اینستاگرام')
    logo = models.ImageField(upload_to=upload_image,null=True,blank=True,verbose_name='تصویر')
    image_thumbnail = ImageSpecField(
        source='logo',
        processors=[ResizeToFill(32,32)],
        format='JPEG',
        options={'quality': 90}
    )

    def __str__(self):
        return 'تنظیمات سایت'

    class Meta:
        verbose_name = 'تنظیمات'
        verbose_name_plural = 'تنظیمات'