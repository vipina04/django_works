from django.contrib import admin
from classroom_app import models
# Register your models here.


admin.site.register(models.Login)
admin.site.register(models.Student)
admin.site.register(models.Complaint)
admin.site.register(models.Notifications)