from idlelib.autocomplete import FILES

from django.contrib import messages, auth
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect

from .forms import NewUserForm
from .models import show, kim, bob, one


# Create your views here.
def new(request):
    a = show.objects.all()
    b = kim.objects.all()

    return render(request, 'poi.html', {'big': a, 'join': b})


def asd(request):
    return render(request, 'color.html')


def register_request(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            messages.success(request, "registered")

            return redirect('mm')

    else:
        form = NewUserForm()

    return render(request, 'register.html', {'register_form': form})


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}.')
                return redirect('lm')
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, 'Invalid username or password')
    form = AuthenticationForm()
    return render(request, 'login.html', {'login_form': form})


def logout_request(request):
    auth.logout(request)

    return redirect('lm')


def wtd(request):
    z = bob.objects.all()

    n = one.objects.all()
    return render(request, 'index.html', {'pop': z, 'op': n})
