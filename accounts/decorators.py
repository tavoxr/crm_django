from django.http import HttpResponse
from django.shortcuts import redirect

# decorators se usan en python para pasar una funcion como parametro dentro de otra funcion para agregarle
#mas funcionalidad a la funcion antes de que se ejecute la funcion

def unauthenticated_user(vie_func):
    def wrapper_func(request, *args, **kwargs):
        
        if request.user.is_authenticated:
            return redirect('home')
        else:
            return vie_func(request, *args, **kwargs)

    return wrapper_func



def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args,**kwargs):

            group = None
            if request.user.groups.exists():
               group = request.user.groups.all()[0].name
               #print('groups: ', group)
               
            if group in allowed_roles:
                return view_func(request, *args, **kwargs)
            else:
                return HttpResponse("You're not authorized to view this page")

        return wrapper_func

    return decorator



def admin_only(view_func):
    def wrapper_func(request, *args,**kwargs):
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
            
        if group == 'customer':
            return redirect('userPage')

        if group == 'admin':
            return view_func(request,*args,**kwargs)
    
    return wrapper_func
