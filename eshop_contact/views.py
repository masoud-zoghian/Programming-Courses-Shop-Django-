from django.shortcuts import render
from eshop_contact.models import ContactUs
from eshop_contact.forms import ContactUsForm
from eshop_settings.models import Settings

# Create your views here.
def contact_us_page(request):
    contact_form = ContactUsForm(request.POST or None)
    if contact_form.is_valid():
        fullName = contact_form.cleaned_data.get('fullName')
        email = contact_form.cleaned_data.get('email')
        message = contact_form.cleaned_data.get('message')
        new_contact = ContactUs.objects.create(fullName=fullName, email=email, message=message)
        print(new_contact)

    setting = Settings.objects.first()

    context = {
        'contact_form':contact_form,
        'setting':setting,
    }
    return render(request, 'contact_us_page.html',context)