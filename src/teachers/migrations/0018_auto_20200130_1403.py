# Generated by Django 2.2.9 on 2020-01-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0017_auto_20200130_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.EmailField(default='i@gmail.com', max_length=254, unique=True),
            preserve_default=False,
        ),
    ]
