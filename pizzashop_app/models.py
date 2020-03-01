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
