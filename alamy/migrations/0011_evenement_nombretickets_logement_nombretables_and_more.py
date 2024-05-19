# Generated by Django 5.0.3 on 2024-05-05 18:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alamy', '0010_alter_poste_utilisateur'),
    ]

    operations = [
        migrations.AddField(
            model_name='evenement',
            name='nombretickets',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='logement',
            name='nombreTables',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='transport',
            name='nombreplaces',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=100)),
                ('prenom', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('date_rendez_vous', models.DateField(blank=True, null=True)),
                ('nombre_places', models.IntegerField(blank=True, null=True)),
                ('telephone', models.CharField(max_length=20)),
                ('date', models.DateField(blank=True, null=True)),
                ('heure', models.TimeField(blank=True, null=True)),
                ('nombre_personnes', models.IntegerField(blank=True, null=True)),
                ('nombre_tickets', models.IntegerField(blank=True, null=True)),
                ('poste', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='reservation', to='alamy.poste')),
            ],
        ),
    ]
