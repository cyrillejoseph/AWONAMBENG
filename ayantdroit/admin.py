from django.contrib import admin
from .models import AyantDroit


class AyantDroitAdmin(admin.ModelAdmin):
    list_display = ('matfil', 'nomayd', 'prenom', 'sexe', 'datnais', 'filiation')
    ordering = ('matfil',)


admin.site.register(AyantDroit, AyantDroitAdmin)
