from django.shortcuts import render, HttpResponse
from datetime import datetime
from myapplication.models import Contact
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request, 'index.html')
def aboutus(request):
    context = {
        'shop_name': 'RDT CANDY SHOP',
        'description': 'Your one-stop shop for delicious handmade candies and chocolates!',
        'specialties': ['Homemade Fudge', 'Gourmet Chocolates', 'Sugar-Free Candies', 'Assorted Jelly Beans']
    }
    return render(request, 'about.html', context)
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        # Create a Contact object and save it
        contact = Contact(
            name=name,
            email=email,
            phone=phone,
            desc=desc,
            date=datetime.today()  # Make sure this is properly set
        )
        contact.save()
        messages.success(request, "Your message has been sent!")
    return render(request, 'contact.html')
def services(request):
    return render(request,'service.html')
def owner(request):
    return render(request,'owner.html')
def buy(request):
    return render(request,'buy.html')
