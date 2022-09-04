from pickletools import read_unicodestring1
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


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
