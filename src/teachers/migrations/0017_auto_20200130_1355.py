# Generated by Django 2.2.9 on 2020-01-30 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0016_auto_20200130_1348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]