from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns=[
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name='userPage' ),
    path('register/', views.register, name="register"),
    path('products/', views.products, name="products"),
    path('customer/<int:pk>/', views.customer, name="customer"),
    path('customer/', views.createCustomer, name= 'createCustomer'),
    path('ordersCreate/<int:pk>/', views.createOrder, name="orders"),
    path('orders/<int:pk>/', views.updateOrder, name='updateOrder'),
    path('ordersDelete/<int:pk>', views.deleteOrder, name="deleteOrder"),
    path('account_settings/', views.accountSettings, name="account_settings"),
    path('reset_password/', auth_views.PasswordResetView.as_view(template_name="accounts/password_reset.html"), name='password_reset'),  # utilizando las clases de django para resetear pass por correo se pone as_view() porque es una base class view
    path('reset_password_sent/', auth_views.PasswordResetDoneView.as_view(template_name= "accounts/password_reset_sent.html"), name='password_reset_done'), # render succes message when password was set
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name= "accounts/password_reset_form.html"), name='password_reset_confirm'), 
    path('reset_password_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="accounts/password_reset_done.html"), name='password_reset_complete'), 
]

#submit email form                          //PasswordResetView
#Email sent success message                 //PasswordResetDoneView
#Link to password Reset form in email       //PasswordResetConfirmView
#Password successfully changed message      //