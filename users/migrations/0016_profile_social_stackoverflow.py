# Generated by Django 3.2.10 on 2021-12-29 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20211229_1144'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='social_stackoverflow',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
