from django.shortcuts import render, HttpResponse
from datetime import datetime
from .models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
    #return HttpResponse('this is home page')

def  Home(request):
    return render(request, 'Home.html')


def  about(request):
    return render(request, 'about.html')
   # return HttpResponse(' about page')

def services(request):
    return render(request, 'services.html')
    #return HttpResponse(' services page')

def contact(request):
    if request.method == 'POST':
        name= request.POST.get('name')
        email= request.POST.get('email')
        password= request.POST.get('password')
        phone = request.POST.get('phone')
        contact = Contact(name=name, phone=phone, email=email, password=password, date=datetime.today())
        contact.save()
        messages.success(request, 'your message has been saved')
    return render(request, 'contact.html')
    
    #return HttpResponse(' contaqct page')        