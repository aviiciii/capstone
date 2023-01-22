from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from capstone.settings import REDIRECT_LOGIN_URL
from django.db import IntegrityError

# json request
from django.http import JsonResponse
from django.http import HttpResponse
import json
from django.core import serializers

# pip install panimalar
from rollno import isvalid

# db
from users.models import User
from db.models import Professor, Student, Class, Semester, Subject


# Create your views here.
def index(request):
    return render(request, 'staff_admin/index.html')

# ----------------- ADD -----------------

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
        
        # check if rollno is valid
        if not isvalid(rollno):
            messages.error(request, 'Invalid roll number')
            return render(request, 'staff_admin/student/add_students.html')


        try:
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
        except IntegrityError as e:
            messages.error(request, 'User already exists')
            return render(request, 'staff_admin/student/add_students.html')
        except:
            messages.error(request, 'Something went wrong while creating user')
            return render(request, 'staff_admin/student/add_students.html')
        
        # create student
        try:
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

        except:
            messages.error(request, 'Something went wrong while creating student but user created')
            return render(request, 'staff_admin/student/add_students.html')
        

        messages.success(request, 'Student added successfully')
        return render(request, 'staff_admin/student/add_students.html')
    
    return render(request, 'staff_admin/student/add_students.html')


@login_required(login_url=REDIRECT_LOGIN_URL)
def add_professor(request):
    if request.method == 'POST':
        print(request.POST)
        # get data
        firstname = request.POST['firstname'].strip().lower().capitalize()
        lastname = request.POST['lastname'].strip().lower().capitalize()
        email = request.POST['email'].strip().lower()
        dept = request.POST['dept'].strip().lower()
        dob = request.POST['dob']
        joining_year = request.POST['joining_year'].strip()
        qualification = request.POST['qualification'].strip().lower().capitalize()

        # join firstname and lastname to create username
        username = f'{firstname} {lastname}'

        try:
            # create user for student
            new_user = User.objects.create_user(
                    username=username, 
                    email=email,
                    password='12345678',
                    role='professor',
                    first_name=firstname,
                    last_name=lastname,
            )
            new_user.save()
            print('User created')
        except IntegrityError as e:
            messages.error(request, 'User already exists')
            return render(request, 'staff_admin/professor/add_professor.html')
        
        except Exception as e:
            messages.error(request, 'Something went wrong while creating user')
            return render(request, 'staff_admin/professor/add_professor.html')


        

        try:
            professor_obj = Professor.objects.create(
                user=new_user,
                dept=dept,
                joining_year=joining_year,
                qualification=qualification,
                dob=dob,
                working=True
            )
            professor_obj.save()
            print('Professor created')
        except:
            messages.error(request, 'Something went wrong while creating professor but user created')
            return render(request, 'staff_admin/professor/add_professor.html')

        

        messages.success(request, 'Professor added successfully')
        return render(request, 'staff_admin/professor/add_professor.html')




    return render(request, 'staff_admin/professor/add_professor.html')


@login_required(login_url=REDIRECT_LOGIN_URL)
def add_subject(request):
    if request.method == 'POST':
        print(request.POST)
        # get data
        name = request.POST['subjectname'].strip().lower().capitalize()
        code = request.POST['subjectcode'].strip().lower()
        regulation = request.POST['regulation'].strip().lower()
        credits = str(request.POST['credits'].strip())
        

        try:
            subject_obj = Subject.objects.create(
                name=name,
                code=code,
                regulation_year=regulation,
                credits=credits,
            )

            subject_obj.save()
            print('Subject created')
        except:
            messages.error(request, 'Something went wrong while creating subject')
            return render(request, 'staff_admin/subject/add_subject.html')

        messages.success(request, 'Subject added successfully')
        return render(request, 'staff_admin/subject/add_subject.html')



    return render(request, 'staff_admin/subject/add_subject.html')

@login_required(login_url=REDIRECT_LOGIN_URL)
def add_class(request):
    if request.method == 'POST':
        print(request.POST)
        # get data
        enrolled_year = request.POST['enrolled_year'].strip().lower()
        dept = request.POST['department'].strip().lower()
        section = request.POST['section'].strip().lower()
        

        try:
            class_obj = Class.objects.create(
                enrolled_year=enrolled_year,
                dept=dept,
                section=section,
            )

            class_obj.save()
            print('Class created')
        except:
            messages.error(request, 'Something went wrong while creating class')
            return render(request, 'staff_admin/class/add_class.html')

        messages.success(request, 'Class added successfully')


    return render(request, 'staff_admin/class/add_class.html')


@login_required(login_url=REDIRECT_LOGIN_URL)
def get_students_for_class_assign(request, class_id):
    if request.method == 'POST':

        classobj = Class.objects.get(pk=class_id)

        enrolled_year = classobj.enrolled_year
        dept = classobj.dept

        # gets students of enrolled year and dept who are studying and not assigned to any class
        student_list = [ student.pk.upper() for student in Student.objects.filter(enrolled_year=enrolled_year, dept=dept, studying=True, class__isnull=True) ]
        present_students = [ student.pk.upper() for student in classobj.students.all() ]
        
    
        return JsonResponse({
            "message":"Change Successful",
            "students": student_list,
            "present_students": present_students,
        })
    
    return JsonResponse({
        "message":"GET request not allowed",
    })


@login_required(login_url=REDIRECT_LOGIN_URL)
def assign_student_to_class(request):

    if request.method == 'POST':
        print(request.POST)
        # get data
        class_id = request.POST['class_id']
        student_rollno = request.POST.getlist('students')
        
        if student_rollno == []:
            messages.error(request, 'No students selected')
            return redirect('assign_student_to_class')
        
        if 'add' in request.POST:
            print('add')
            classobj = Class.objects.get(pk=class_id)
            for rollno in student_rollno:
                studentobj = Student.objects.get(pk=rollno.lower())
                classobj.students.add(studentobj)
            classobj.save()
            messages.success(request, 'Students added successfully')
            return redirect('assign_student_to_class')

        elif 'remove' in request.POST:
            print('remove')
            classobj = Class.objects.get(pk=class_id)
            for rollno in student_rollno:
                studentobj = Student.objects.get(pk=rollno.lower())
                classobj.students.remove(studentobj)
            classobj.save()
            messages.success(request, 'Students removed successfully')
            return redirect('assign_student_to_class')
        
        else:
            print('else')
            messages.error(request, 'Something went wrong')
            return redirect('assign_student_to_class')
        
        
        # get class object
        classobj = Class.objects.get(pk=class_id)

    
    
    classes = Class.objects.all()

    context = {'classes': classes}

    return render(request, 'staff_admin/class/assign_students_to_class.html', context)















def assign_courses_to_batches(request):
    pass

def assign_professor_to_subjects(request):
    pass

def make_timetable(request):
    pass

def edit_timetable(request):
    pass

def edit_student(request):
    pass

def edit_professor(request):
    pass

def edit_courses(request):
    pass

def edit_batches(request):
    pass

def edit_subjects(request):
    pass

def mark_attendance(request):
    pass

def substitute_attendance(request):
    pass

def edit_attendance(request):
    pass

def view_attendance(request):
    pass

def view_student_attendance(request):
    pass

def view_professor_attendance(request):
    pass
