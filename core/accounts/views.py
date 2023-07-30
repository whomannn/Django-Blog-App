from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import CustomUserCreationForm
# Create your views here.

def loginview(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request,email=email,password=password)
        if user is not None:
            login(request,user)
            return render(request,'home.html')
        else:
            context = {
                "error" : "Invalid email or password."
            }
            return render(request,"login.html",context)
    else:
        return render(request,"login.html",{})
    
def signupview(request):
    if request.method == "GET":
        form = CustomUserCreationForm()
        return render(request, "signup.html", {"form": form})
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = user.email.lower()
            user.save()
            messages.success(request, "You have singed up successfully.")
            login(request, user)
            return redirect("/blog")
        else:
            return render(request, "signup.html", {"form": form})