from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# from .forms import CreateUserForm


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        # form = CreateUserForm()
        form='jj'
        if request.method == 'POST':
            # form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'users/register.html', context)

def index(request):
    return render(request, 'users/index.html')