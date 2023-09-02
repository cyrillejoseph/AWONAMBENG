from django.contrib import admin
from .models import Personnel


class PersonnelAdmin(admin.ModelAdmin):
    list_display = ('matric', 'nompers', 'prenom', 'sexe', 'datnais', 'sitfam', 'nbrenf')
    ordering = ('matric',)


admin.site.register(Personnel, PersonnelAdmin)
