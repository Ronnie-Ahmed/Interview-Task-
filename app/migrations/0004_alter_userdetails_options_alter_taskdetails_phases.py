# Generated by Django 5.0 on 2024-01-08 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_alter_taskdetails_options_alter_taskdetails_phases_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='userdetails',
            options={'verbose_name': 'User Details', 'verbose_name_plural': 'User Details'},
        ),
        migrations.AlterField(
            model_name='taskdetails',
            name='phases',
            field=models.CharField(choices=[('Backlog', 'Backlog'), ('ToDo', 'ToDo'), ('Completion', 'Completion'), ('InProgress', 'InProgress')], max_length=15),
        ),
    ]