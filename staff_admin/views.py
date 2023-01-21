from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from capstone.settings import REDIRECT_LOGIN_URL

# db
from users.models import User
from db.models import Professor, Student, Class, Semester, Subject


# Create your views here.
def index(request):
    return render(request, 'professor/index.html')



@login_required(login_url=REDIRECT_LOGIN_URL)
def add_student(request):

    if request.method == 'POST':
        print(request.POST)
        # get data
        firstname = request.POST['firstname'].strip().lower().capitalize()
        lastname = request.POST['lastname'].strip().lower().capitalize()
        email = request.POST['email'].strip().lower()
        rollno = request.POST['rollno'].strip().lower()
        dept = request.POST['dept'].strip().lower()
        dob = request.POST['dob']
        enrolled_year = request.POST['enrolled_year'].strip()

        # join firstname and lastname to create username
        username = f'{firstname} {lastname}'

        # create user for student
        new_user = User.objects.create_user(
                username=username, 
                email=email,
                password='12345678', 
                role='student',
                first_name=firstname,
                last_name=lastname,
        )
        
        new_user.save()
        print('user created')


        student_obj = Student.objects.create(
            user=new_user,
            roll_no=rollno,
            dept=dept,
            enrolled_year=enrolled_year,
            dob=dob,
            studying=True
        )

        student_obj.save()
        print('student created')
        

        messages.success(request, 'Student added successfully')
        return render(request, 'professor/add_students.html')
    
    return render(request, 'professor/add_students.html')

