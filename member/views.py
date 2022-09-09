from pickletools import read_unicodestring1
from wsgiref.util import request_uri
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.http import JsonResponse
from store.models import Customer
from . import views
import json
from django.contrib.auth.models import User


def login_user(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('store')
            # Redirect to a success page.

        else:
            messages.success(request, "There was invalid input")
            return redirect('login')
    else:
        context = {}
        return render(request, 'authentication/login.html', context)

# Create your views here.


def logout_user(request):
    logout(request)
    messages.success(request, "You were Logged Out!")
    return redirect('store')


def register_user(request):
    # if request.method == "POST":
    #     form = UserCreationForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         username = form.cleaned_data['username']
    #         password = form.cleaned_data['password']
    #         user = authenticate(username=username, password=password)
    #         print(request.data)
    #         login(request, user)
    #         messages.success(request, ("Registeration successful"))
    #         redirect('store')
    #         customer, created = Customer.objects.get_or_create()
    #         customer.name = username
    #         customer.save()
    #     else:
    #         print('invalid')
    # else:
    #     form = UserCreationForm()
    # {'form': form})
    return render(request, 'authentication/register_user.html', {})


def create_customer(request):
    data = json.loads(request.body)
    user = User.objects.create_user(username=data['form']['name'],
                                    email=data['form']['email'],
                                    password=data['form']['password'])
    customer, created = Customer.objects.get_or_create(
        user=user,
        email=data['form']['email'],
        name=data['form']['name'],
    )
    customer.save()
    login(request, user)
    return JsonResponse('Create User Success', safe=False)

# user = models.OneToOneField(
#         User, on_delete=models.CASCADE, null=True, blank=True)
#     name = models.CharField(max_length=200, null=True)
#     email = models.CharField(max_length=200, null=True)
