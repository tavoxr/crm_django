from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm #para crear utilizar el formulario que creamos para creacion de Usuarios
from django.contrib.auth import authenticate, login, logout # para la autencicacion de login de usuarios
from django.forms import inlineformset_factory
from .forms import *
from .models import *
from .filters import *
from django.contrib import messages

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




def loginPage(request):
    context = {
        'messageType': 'danger'
    }

    if request.method == "POST":
        username = request.POST.get('username')
        password =  request.POST.get('password')

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request,'Username or Password is incorrect')
            return render(request,'accounts/login.html', context )

    return render(request,'accounts/login.html' )


def logoutUser(request):
    logout(request)
    return redirect('login')


def register(request):
    form = CreateUserForm()
    context={
        'form': form
    }
    
    if request.method == "POST":
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')  #permite obtener el atributo username sin otro atributo del formulario createUserForm
            messages.success(request, 'Account was created for ' + user)
            return redirect('login')
    
    return render(request, 'accounts/register.html', context)



