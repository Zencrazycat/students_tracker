# Generated by Django 2.2.9 on 2020-01-19 11:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0007_auto_20200119_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='name',
        ),
    ]
