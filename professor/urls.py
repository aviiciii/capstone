from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='professor_home'),
    # path('profile/', views.profile, name='professor_profile'),
    path('add/student', views.add_student, name='add_student'),
]