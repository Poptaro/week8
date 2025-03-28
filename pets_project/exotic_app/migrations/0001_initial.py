# Generated by Django 5.1.7 on 2025-03-28 18:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('owner_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exotic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('age', models.BigIntegerField()),
                ('vaccinated', models.BooleanField()),
                ('type_of_animal', models.CharField(max_length=255)),
                ('region_of_origin', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='exotic', to='owner_app.owner')),
            ],
        ),
    ]
