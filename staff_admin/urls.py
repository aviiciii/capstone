from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='admin_home'),
    # path('profile/', views.profile, name='professor_profile'),
    path('add/student', views.add_student, name='add_student'),
    path('add/professor', views.add_professor, name='add_professor'),
    path('add/subject', views.add_subject, name='add_subject'),
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