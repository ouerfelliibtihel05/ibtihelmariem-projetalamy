# Generated by Django 5.0.3 on 2024-05-12 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('alamy', '0012_alter_reservation_poste'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reservation',
            old_name='nombre_personnes',
            new_name='nombre_Tables4',
        ),
    ]
