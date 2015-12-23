from django.contrib import admin
from .models import *
from django.contrib.auth.models import User



class ClientAdmin(admin.ModelAdmin):
    list_display = ('clientname', 'projects')

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('projectname','courses')

admin.site.register(Clients,ClientAdmin)
admin.site.register(Projects,ProjectAdmin)
admin.site.register(Courses)
admin.site.register(User_Timesheet)
admin.site.register(Department)

