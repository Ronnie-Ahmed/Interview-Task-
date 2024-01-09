# Generated by Django 5.0 on 2024-01-08 13:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=10)),
                ('userpic', models.ImageField(upload_to='photos')),
            ],
        ),
        migrations.CreateModel(
            name='TaskDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('taskname', models.CharField(max_length=10000)),
                ('phases', models.CharField(choices=[('ToDo', 'ToDo'), ('Completion', 'Completion'), ('Backlog', 'Backlog'), ('InProgress', 'InProgress')], max_length=15)),
                ('completed_at', models.DateTimeField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.userdetails')),
            ],
        ),
    ]