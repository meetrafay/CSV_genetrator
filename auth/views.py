# yourapp/views.py
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login

from auth.utils import send_welcome_email
from .forms import HomeForm, LoginForm

from django.contrib import messages
from django.contrib.auth import logout 

def login_view(request):
    if request.method == 'POST':
        print("==>")
        form = LoginForm(request.POST)
        if form.is_valid():
            print("----->>")
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # a = send_welcome_email(request)
                # print(a,"==>")
                # messages.success(request, 'You are logged in successfully.')
                return redirect('/auth/home/') 
            else:
                messages.error(request, 'Invalid username or password.')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = LoginForm()

    return render(request, 'auth/login.html', {'form': form})

@login_required
def home(request):
    success_message = None
    if request.method == 'POST':
        form = HomeForm(request.POST)
        if form.is_valid():
            # Get form data
            email = form.cleaned_data['email']
            option = form.cleaned_data['option']
           
            send_welcome_email(email)
            success_message = 'Email sent successfully!'
    else:
        form = HomeForm()

    return render(request, 'auth/home.html', {'form': form, 'success_message': success_message})


def logout_view(request):
    logout(request)
    return redirect('login')
