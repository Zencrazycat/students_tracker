# Generated by Django 2.2.9 on 2020-01-20 20:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0001_initial'),
        ('students', '0012_auto_20200120_2010'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='curator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='teachers.Teacher'),
        ),
    ]
