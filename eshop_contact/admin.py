from django.contrib import admin
from eshop_contact.models import ContactUs

# Register your models here.
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['__str__','fullName','email','read']

    class Meta:
        model = ContactUs

admin.site.register(ContactUs, ContactUsAdmin)