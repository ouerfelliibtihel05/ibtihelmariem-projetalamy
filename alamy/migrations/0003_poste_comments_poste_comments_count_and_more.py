# Generated by Django 5.0.3 on 2024-04-21 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alamy', '0002_stage_lieu'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='comments',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='poste',
            name='comments_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poste',
            name='dislikes_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='poste',
            name='ikes_count',
            field=models.IntegerField(default=0),
        ),
    ]
