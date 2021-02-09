from django.db import models

# Create your models here.

class Customer(models.Model):
    name= models.CharField(max_length=200)
    phone =  models.CharField(max_length=15)
    email = models.EmailField(max_length=100)
    date_created = models.DateTimeField(auto_now_add  = True)

    def __str__(self):
        return f'{self.name}'

class Tag(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name

class Product(models.Model):
    CATEGORY= [
        ('INDOOR', 'Indoor'),
        ('OUT DOOR', 'Out Door'),
    ]
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=9, decimal_places=2, blank=True)
    category= models.CharField(max_length=10, choices= CATEGORY, default='INDOOR')
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return f'{self.name} '

class Order(models.Model):
    
    STATUS = [
        ('DELIVERED','DELIVERED'),
        ('SENDING','SENDING'),
        ('PENDING','PENDING'),
    ]
    customer = models.ForeignKey(Customer, on_delete = models.CASCADE)
    product = models.ForeignKey(Product, on_delete = models.CASCADE)
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=12, choices=STATUS, default='PENDING' )

    def __str__(self):
        return f'Order No. {self.id}, Customer: {self.customer.name}, Product: {self.product.name}'