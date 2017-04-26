# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-26 16:00
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('revendication', '0008_evenement_titre'),
    ]

    operations = [
        migrations.CreateModel(
            name='Petition',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.TextField(verbose_name='Descrition de la pétition')),
                ('date_creation', models.DateField(auto_now=True, verbose_name='Date de création')),
                ('date_echeance', models.DateField(blank=True, null=True, verbose_name="Date d'échéance")),
                ('objectif_de_signataires', models.IntegerField(blank=True)),
                ('propositions', models.ManyToManyField(null=True, to='revendication.Proposition')),
                ('signataires', models.ManyToManyField(null=True, through='revendication.Soutien', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RenameField(
            model_name='evenement',
            old_name='Titre',
            new_name='titre',
        ),
        migrations.AddField(
            model_name='soutien',
            name='petition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='revendication.Petition'),
        ),
    ]
