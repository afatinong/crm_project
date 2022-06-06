import imp
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    print("hello")
    return render(request, 'accounts/dashboard.html')

def products(request):
    print("hi")
    return render(request, 'accounts/products.html')
    

def customer(request):
    return HttpResponse('accounts/customer.html')
