# Generated by Django 4.2.4 on 2023-09-02 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ayantdroit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ayantdroit',
            name='nomayd',
            field=models.CharField(max_length=100, null=True, verbose_name='Nom Ayant Droit'),
        ),
        migrations.AlterField(
            model_name='ayantdroit',
            name='prenom',
            field=models.CharField(max_length=100, null=True, verbose_name='Prénom Ayant Droit'),
        ),
    ]
