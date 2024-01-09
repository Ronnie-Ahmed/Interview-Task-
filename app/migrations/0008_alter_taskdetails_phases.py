# Generated by Django 5.0 on 2024-01-08 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_taskdetails_phases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetails',
            name='phases',
            field=models.CharField(choices=[('Backlog', 'Backlog'), ('ToDo', 'ToDo'), ('InProgress', 'InProgress'), ('Completion', 'Completion')], max_length=15),
        ),
    ]