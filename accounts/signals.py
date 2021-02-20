from os import name
from django.contrib.auth.models import User, Group
from .models import Customer
from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender=User)
def create_customer_profile(sender,instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')    
        instance.groups.add(group) #para agregar el grupo directamente al registrar usuario, customer en este caso

        Customer.objects.create(
            user= instance,
            name =  instance.username
        )
        
        print('Profile created')


# @receiver(post_save, sender=User)
# def update_customer_profile(sender, instance, created, **kwargs):
#     if created == False:
#         instance.customer.save()
#         print('Profile Updated')
