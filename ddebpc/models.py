from django.contrib.auth.models import User
from django.db import models
from personnel.models import Personnel
from ayantdroit.models import AyantDroit


class DdeBpc(models.Model):
    RELATION = (('moi meme', 'moi meme'),
                ('mon épouse', 'mon épouse'),
                ('mon époux', 'mon époux'),
                ('ma fille', 'ma fille'),
                ('mon fils', 'mon fils'))
    STATUS = (('crée', 'crée'),
              ('modifié', 'modifié'),
              ('supprimé', 'supprimé'),
              ('validé', 'validé'))
    socaff = models.CharField(max_length=100, verbose_name='Société')
    centre = models.CharField(max_length=30, verbose_name="Centre")
    email = models.EmailField(max_length=50, null=True, verbose_name="Email")
    personnel = models.ForeignKey(Personnel, null=True, on_delete=models.CASCADE, verbose_name='Employé')
    flaydrt = models.BooleanField(default=False, verbose_name='Ayant Droit ?')
    ayantdroit = models.ForeignKey(AyantDroit, blank=True, null=True, on_delete=models.SET_NULL, verbose_name='Nom Ayant Droit')
    relation = models.CharField(max_length=20, null=True, choices=RELATION, verbose_name="Filiation avec l'employé")
    status = models.CharField(max_length=20, null=True, choices=STATUS, verbose_name='Statut')
    datcreat = models.DateTimeField(blank=True, null=True, auto_now_add=True, verbose_name='Créer le')
    nomcreat = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, verbose_name='Par')

    def __str__(self):
        return self.personnel
