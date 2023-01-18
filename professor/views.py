from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'professor/index.html')


def add_student(request):
    return render(request, 'professor/add_students.html')

