# Generated by Django 5.0.3 on 2024-04-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alamy', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stage',
            name='lieu',
            field=models.CharField(default='', max_length=100),
        ),
    ]
