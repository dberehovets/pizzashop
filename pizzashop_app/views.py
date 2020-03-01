from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from pizzashop_app.forms import UserForm, PizzaShopForm

# Create your views here.


def home(request):
    return redirect(pizzashop_home)


@login_required(login_url="pizzashop/sign-in")
def pizzashop_home(request):
    return render(request, 'pizzashop_app/home.html')


def pizzashop_sign_up(request):
    user_form = UserForm()
    pizzashop_form = PizzaShopForm()
    return render(request, 'pizzashop_app/sign_up.html', {'user_form': user_form,
                                                          'pizzashop_form': pizzashop_form})