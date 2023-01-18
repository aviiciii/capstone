from django.contrib import admin
from . import models
# Register your models here.

admin.site.register(models.Professor)
admin.site.register(models.LabAssistant)
admin.site.register(models.Student)
admin.site.register(models.Class)
admin.site.register(models.Semester)
admin.site.register(models.Subject)
