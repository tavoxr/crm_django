from django.shortcuts import render

from django.http import HttpResponse

from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    totalOrders= orders.count()
    deliveredOrders = Order.objects.filter(status = "DELIVERED").count()
    pendingOrders = orders.filter(status = "PENDING").count()
    customers = Customer.objects.all()
    last5Orders = orders.order_by('-date_created')
    data={
        'orders': orders,
        'totalOrders': totalOrders,
        'deliveredOrders': deliveredOrders,
        'pendingOrders': pendingOrders,
        'customers': customers,
        'last5Orders': last5Orders,
    }

    return render(request, 'accounts/dashboard.html', data)

def products(request):

    products = Product.objects.all()
    data = {'products': products}
    # if request.method == "GET":

    return render(request,'accounts/products.html',data)

def customer(request,pk):
    customer = Customer.objects.get(id = pk)
    orders = customer.order_set.all()
    totalOrders = orders.count()
    
    context = {
        'customer': customer,
        'orders': orders,
        'totalOrders': totalOrders
    }
    return render(request,'accounts/customer.html', context)
