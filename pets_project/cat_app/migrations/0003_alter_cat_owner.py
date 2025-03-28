# Generated by Django 5.1.7 on 2025-03-28 19:04

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cat_app', '0002_alter_cat_owner'),
        ('owner_app', '0002_remove_owner_number_of_pets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cat',
            name='owner',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='cats', to='owner_app.owner'),
        ),
    ]
