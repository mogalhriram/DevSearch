# Generated by Django 3.2.10 on 2021-12-29 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0010_profile_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='created',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='description',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='name',
        ),
        migrations.RemoveField(
            model_name='skill',
            name='owner',
        ),
        migrations.AlterField(
            model_name='skill',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
