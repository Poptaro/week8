# Generated by Django 5.1.7 on 2025-03-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_app', '0009_alter_subject_students'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='students',
            field=models.ManyToManyField(related_name='subject', to='student_app.student'),
        ),
    ]
