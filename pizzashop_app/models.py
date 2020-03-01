from django.db.models import *
from django.contrib.auth.models import User


class PizzaShop(Model):
    owner = OneToOneField(User, on_delete=CASCADE, related_name='pizzashop')
    name = CharField(max_length=100)
    phone = CharField(max_length=100)
    address = CharField(max_length=100)
    logo = ImageField(upload_to='pizzashop_logo/', blank=False)

    def __str__(self):
        return self.name
