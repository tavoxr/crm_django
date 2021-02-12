from django.shortcuts import render, redirect

from django.http import HttpResponse

from django.forms import inlineformset_factory
from .forms import *
from .models import *
from .filters import *
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
    myFilter = OrderFilter(request.GET, queryset= orders)
    orders = myFilter.qs
    context = {
        'customer': customer,
        'orders': orders,
        'totalOrders': totalOrders,
        'myFilter': myFilter
    }
    return render(request,'accounts/customer.html', context)


def createOrder(request, pk):
    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=5)
    customer = Customer.objects.get(id=pk)
    formSet = OrderFormSet(queryset= Order.objects.none(), instance= customer)
    # form = OrderForm(initial={'customer': customer})
    context = {
        'formSet': formSet,
        'option': 'Create'
    }
    if request.method == "POST":
        print('request.POST', request.POST)

        formSet = OrderFormSet(request.POST, instance= customer)
        # form =OrderForm(request.POST)

        if formSet.is_valid():
            formSet.save()
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




def login(request):

    context={
        'login': 'login'
    }
    return render(request,'accounts/login.html',context )


def register(request):
    context={
        'register': 'register'
    }
    
    return render(request, 'accounts/register.html', context)



