from django.db import models
from django.contrib.auth.models import User


class Employe(models.Model):
    STATUS = (('actif', 'actif'),
              ('suspendu', 'suspendu'),
              ('licencié', 'licencié'))
    matric = models.CharField(max_length=6, verbose_name="Matricule", unique=True)
    nompers = models.CharField(max_length=50, null=True, verbose_name="Nom de l'employé")
    prenom = models.CharField(max_length=50, null=True, verbose_name="Prenom de l'employé")
    centre = models.CharField(max_length=30, null=True, verbose_name="Centre")
    email = models.EmailField(max_length=50, null=True, verbose_name="Email")
    status = models.CharField(max_length=20, null=True, choices=STATUS, verbose_name="Statut")
    datcreat = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='Créer le')
    nomcreat = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Par')
    datmodif = models.CharField(max_length=20, null=True, verbose_name="Modifié le")

    def __str__(self):
        return self.nompers
