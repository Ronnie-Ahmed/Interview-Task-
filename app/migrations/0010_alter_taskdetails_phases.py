# Generated by Django 5.0 on 2024-01-09 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_taskdetails_phases_alter_userdetails_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskdetails',
            name='phases',
            field=models.CharField(choices=[('ToDo', 'ToDo'), ('Backlog', 'Backlog'), ('Doing', 'Doing'), ('Completion', 'Completion')], max_length=15),
        ),
    ]
