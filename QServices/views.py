from itertools import product

from django.http import HttpResponse
from django.shortcuts import render
from .models import Service
from  QProducts.models import Product
from  BookStore.models import Book

# Create your views here.
def home_view(request):
        services=Service.objects.all()[:4]
        products=Product.objects.all()[:4]
        books=Book.objects.all()[:4]
        return render(request,'home.html',{'services':services,'products':products,'books':books})
def services_page(request):
        services = Service.objects.all()
        books=Book.objects.all()
        return render(request, 'services.html', {'services': services,'books':books })