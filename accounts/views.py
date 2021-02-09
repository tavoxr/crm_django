from django.shortcuts import render, redirect

from django.http import HttpResponse

from .forms import *
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


def createOrder(request):
    form = OrderForm()
    context = {
        'form': form,
        'option': 'Create'
    }
    if request.method == "POST":
        print('request.POST', request.POST)

        form =OrderForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    

    return render(request,'accounts/orderForm.html', context)


def updateOrder(request,pk):
    order =  Order.objects.get(id=pk)
    form = OrderForm(instance = order)
    context={
        'form': form,
        'option': 'Edit'
    }
    if request.method == 'POST':
        form = OrderForm(request.POST, instance= order)
        if form.is_valid():
            form.save()
            return redirect('home')

    return render(request, 'accounts/orderForm.html',context)


def deleteOrder(request,pk):
    order =  Order.objects.get(id= pk)
    context= {
        'order':order
    }


    if request.method =='POST':
        order.delete()        
        return redirect('home')

    return render(request, 'accounts/delete.html', context)



def createCustomer(request):
    form = CustomerForm()    
    context = {
        'form': form,
        'option': 'Create'
    }

    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        
    return render(request, 'accounts/customerForm.html', context)








