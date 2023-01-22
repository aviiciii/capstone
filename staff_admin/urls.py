from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='admin_home'),
    # path('profile/', views.profile, name='professor_profile'),
    path('add/student', views.add_student, name='add_student'),
    path('add/professor', views.add_professor, name='add_professor'),
    path('add/subject', views.add_subject, name='add_subject'),
    path('add/class', views.add_class, name='add_class'),
    path('add/semester', views.add_semester, name='add_semester'),
    # assign stuents to class
    path('assign/student_to_class', views.assign_student_to_class, name='assign_student_to_class'),
    path('assign/class/<int:class_id>', views.get_students_for_class_assign, name='get_students_for_class_assign'),
]

# to do

# add student --> done
# add professor
# add courses
# add batches
# assign student to batches
# assign courses to batches -> subjects
# assign professor to subjects
# make timetable
# edit timetable
# edit student
# edit professor
# edit courses
# edit batches
# edit subjects
# mark attendance
# substitute attendance
# edit attendance
# view attendance
# view student attendance
# view professor attendance