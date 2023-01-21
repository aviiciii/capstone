from django.db import models
from users.models import User

# Create your models here.
class Professor(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=100, null=True, blank=True)
    working = models.BooleanField(default=True)
    dob = models.DateField(null=True, blank=True)
    joining_year = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.user.username
    

class LabAssistant(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    qualification = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=100, null=True, blank=True)
    working = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username


class Student(models.Model):
    roll_no = models.CharField(max_length=100, primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    dept = models.CharField(max_length=100, null=True, blank=True)
    enrolled_year = models.CharField(max_length=100, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    studying = models.BooleanField(default=True)

    def __str__(self):
        return self.roll_no
    

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    enrolled_year = models.CharField(max_length=100, null=True, blank=True)
    dept = models.CharField(max_length=100, null=True, blank=True)
    section = models.CharField(max_length=100, null=True, blank=True)
    students = models.ManyToManyField('Student')

    class Meta:
        verbose_name_plural = 'Classes'

    def __str__(self):
        return f'{self.dept}: {self.enrolled_year}-{self.section}'
    

class Semester(models.Model):
    id = models.AutoField(primary_key=True)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    number = models.CharField(max_length=100, null=True, blank=True)
    subjects = models.ManyToManyField('Subject')

    def __str__(self):
        return f'{self.number} ({self.subjects})'
    

class Subject(models.Model):
    code = models.CharField(primary_key=True, max_length=100)
    regulation_year = models.CharField(max_length=10, null=True, blank=True)
    name = models.CharField(max_length=100, null=True, blank=True)
    credits = models.CharField(max_length=100, null=True, blank=True)
    # type ---- Theory, Lab, Project
    type = models.CharField(choices=(('Theory', 'Theory'), ('Lab', 'Lab'), ('Project', 'Project')), max_length=100, null=True, blank=True)

    def __str__(self):
        return f'{self.name} ({self.code})'
    

class SubjectClass(models.Model):
    id = models.AutoField(primary_key=True)
    semester = models.ForeignKey('Semester', on_delete=models.CASCADE)
    subject = models.ForeignKey('Subject', on_delete=models.CASCADE)
    class_name = models.ForeignKey('Class', on_delete=models.CASCADE)
    professor = models.ForeignKey('Professor', on_delete=models.CASCADE)
    lab_assistant = models.ForeignKey('LabAssistant', on_delete=models.CASCADE, null=True, blank=True)
    
    def __str__(self):
        return f'{self.subject} ({self.class_name})'


class TimeTable(models.Model):
    id = models.AutoField(primary_key=True)
    subject_class = models.ForeignKey('SubjectClass', on_delete=models.CASCADE)
    date=models.DateField()
    day = models.CharField(choices=(('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')), max_length=100, null=True, blank=True)
    period = models.CharField(max_length=100, null=True, blank=True)
    completed = models.BooleanField(default=False)
    


class Attendance(models.Model):
    id = models.AutoField(primary_key=True)
    subject_class = models.ForeignKey('SubjectClass', on_delete=models.CASCADE)
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    date = models.DateField()
    present = models.BooleanField(default=False)
    
