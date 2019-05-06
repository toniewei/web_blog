from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import registerform
from django.contrib.auth.decorators import login_required
# Create your views here.

def register(request):

    if request.method == "POST":
        form = registerform(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'success account creation for {username}, you can log in now')
            return redirect('login')
    else:
        form = registerform()
    return render(request, 'users/register.html', context={'form':form})

@login_required
def profile(request):
    return render(request,'users/profile.html')
