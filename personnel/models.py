from django.db import models
from django.contrib.auth.models import User


class Personnel(models.Model):
    matric = models.CharField(max_length=6, verbose_name="Matricule", unique=True)
    nompers = models.CharField(max_length=50, null=True, verbose_name="Nom de l'employé")
    prenom = models.CharField(max_length=50, null=True, verbose_name="Prénom de l'employé")
    sexe = models.CharField(max_length=10, verbose_name="Sexe")
    datnais = models.CharField(max_length=20, null=True, verbose_name="Date Naiss")
    sitfam = models.CharField(max_length=20, null=True, verbose_name="Sit. Fam")
    nbrenf = models.CharField(max_length=10, null=True, verbose_name="Nbre Enf")
    statut = models.CharField(max_length=10, null=True, verbose_name="Statut")
    datcreat = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='Créé le')
    nomcreat = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Par')
    datmodif = models.CharField(max_length=20, null=True, verbose_name="Modifié le")

    def __str__(self):
        return self.nompers
