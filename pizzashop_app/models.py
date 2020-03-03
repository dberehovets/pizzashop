from django.db.models import *
from django.contrib.auth.models import User


class PizzaShop(Model):
    owner = OneToOneField(User, on_delete=CASCADE, related_name='pizzashop')
    name = CharField(max_length=100, verbose_name="Назва піцерії")
    phone = CharField(max_length=100, verbose_name="Телефон")
    address = CharField(max_length=100, verbose_name="Адреса")
    logo = ImageField(upload_to='pizzashop_logo/', blank=False, verbose_name="Логотип")

    def __str__(self):
        return self.name


class Pizza(Model):
    pizzashop = ForeignKey(PizzaShop, on_delete=CASCADE)
    name = CharField(max_length=30)
    short_description = CharField(max_length=100)
    image = ImageField(upload_to='pizza_images', blank=False)
    price = IntegerField(default=0)

    def __str__(self):
        return self.name
