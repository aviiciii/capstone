# Generated by Django 4.1 on 2023-01-21 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('db', '0003_remove_student_id_alter_attendance_id_alter_class_id_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Attendance',
        ),
    ]
