from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.urls import reverse
from users.forms import MyUserCreationForm

from products.models import Products
from .models import User

def home_page(request):
    return render(request, 'home.html', context={})

def register(request):
    if request.method == 'GET':
        return render (request, 'users/register.html', {'form': MyUserCreationForm})
    elif request.method == 'POST':
        form = MyUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect (reverse('templates/home.html'))

def index_page(request):
    if request.user.is_authenticated:
        the_user = User.objects.get(user_name = request.user.username)
        return render(request, 'home.html', context={'the_user':the_user})
    else:
        the_products = Products.objects.all()
    return render(request, 'home.html', context={'products': the_products})