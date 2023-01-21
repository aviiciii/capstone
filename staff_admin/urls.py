from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='admin_home'),
    # path('profile/', views.profile, name='professor_profile'),
    path('add/student', views.add_student, name='add_student'),
    
]