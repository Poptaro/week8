# Generated by Django 5.1.7 on 2025-03-28 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('owner_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='owner',
            name='number_of_pets',
        ),
    ]
