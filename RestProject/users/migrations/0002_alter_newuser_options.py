# Generated by Django 3.2.6 on 2021-08-22 19:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='newuser',
            options={'verbose_name': 'User', 'verbose_name_plural': 'User Table'},
        ),
    ]
