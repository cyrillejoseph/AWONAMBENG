from django.db import models
from django.contrib.auth.models import User


class AyantDroit(models.Model):
    matfil = models.CharField(max_length=9, verbose_name='Matricule', unique=True)
    nomayd = models.CharField(max_length=100, null=True, verbose_name='Nom Ayant Droit')
    prenom = models.CharField(max_length=100, null=True, verbose_name='Prénom Ayant Droit')
    sexe = models.CharField(max_length=10, verbose_name="Sexe")
    datnais = models.CharField(max_length=20, null=True, verbose_name="Date Naiss.")
    filiation = models.CharField(max_length=20, null=True, verbose_name='Filiation')
    statut = models.CharField(max_length=10, null=True, verbose_name="Statut")
    datcreat = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='Créer le')
    nomcreat = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Par')
    datmodif = models.CharField(max_length=20, null=True, verbose_name="Modifie le")

    def __str__(self):
        return self.nomayd
