from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .models import Contact
from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

def contact_page(request):

    if request.method == 'POST':

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone', '')
        city = request.POST.get('city', '')
        service_type = request.POST.get('service_type', '')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            phone=phone,
            city=city,
            service_type=service_type,
            message=message
        )

        messages.success(request, "Your message has been sent successfully!")

        return redirect('contact')

    return render(request, 'contact.html')