# Generated by Django 2.2.9 on 2020-01-29 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0005_auto_20200128_1329'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='academic_degree',
            field=models.PositiveSmallIntegerField(choices=[('m', 'Master'), ('phd', 'Ph.D'), ('md', 'M.D'), ('jd', 'J.D.')], default=None),
        ),
    ]
