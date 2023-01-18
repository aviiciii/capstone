from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from capstone.settings import REDIRECT_LOGIN_URL

# Create your views here.
def index(request):
    return render(request, 'professor/index.html')



@login_required(login_url=REDIRECT_LOGIN_URL)
def add_student(request):

    if request.method == 'POST':
        print(request.POST)
        # get data
        name = request.POST['name']
        email = request.POST['email']
        rollno = request.POST['rollno']
        dept = request.POST['dept']
        dob = request.POST['dob']
        enrolled_year = request.POST['enrolled_year']
        print(type(dob))
        # create user
        user = User.objects.create_user(username=name, email=email, password='12345678')

        messages.success(request, 'Student added successfully')
        return render(request, 'professor/add_students.html')
    
    return render(request, 'professor/add_students.html')

