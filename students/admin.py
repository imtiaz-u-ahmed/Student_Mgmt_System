from django.contrib import admin
from .models import StudentsInfo, GuardianInfo
# Register your models here.

class GuardianAdmin(admin.ModelAdmin):
    list_display = ('name', 'gender', 'age', 'relation', 'phone')

admin.site.register(GuardianInfo,GuardianAdmin)

class studentAdmin(admin.ModelAdmin):
    list_display = ('roll', 'std_class', 'name')

admin.site.register(StudentsInfo,studentAdmin)
