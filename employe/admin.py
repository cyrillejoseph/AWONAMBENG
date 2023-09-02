from django.contrib import admin
from .models import Employe


class EmployeAdmin(admin.ModelAdmin):
    list_display = ('matric', 'nompers', 'prenom', 'centre', 'email', 'status', 'datcreat')
    ordering = ('matric',)


admin.site.register(Employe, EmployeAdmin)
