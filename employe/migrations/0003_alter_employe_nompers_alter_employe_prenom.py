# Generated by Django 4.2.4 on 2023-09-02 22:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employe', '0002_alter_employe_matric'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employe',
            name='nompers',
            field=models.CharField(max_length=50, null=True, verbose_name="Nom de l'employé"),
        ),
        migrations.AlterField(
            model_name='employe',
            name='prenom',
            field=models.CharField(max_length=50, null=True, verbose_name="Prenom de l'employé"),
        ),
    ]
