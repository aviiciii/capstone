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
    return render(request, 'staff_admin/index.html')



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




















def add_courses(request):
    pass

def add_batches(request):
    pass

def assign_student_to_batches(request):
    pass

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
