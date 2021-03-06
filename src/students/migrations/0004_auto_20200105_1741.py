# Generated by Django 2.2.9 on 2020-01-05 17:41

from django.db import migrations, models


def forward(apps, schema_editor):
    Student = apps.get_model('students', 'Student')
    for student in Student.objects.all().only('id', 'telephone').iterator():
                                                                # чтоб экономить память и загружать частично
        student.telephone = ''.join(x for x in student.telephone if x.isdigit())
        student.save(update_fields=['telephone'])
        # изменяем не всю базу а лишь поле телефона (оптимизация)

class Migration(migrations.Migration):

    dependencies = [
        ('students', '0003_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='unique_code',
        ),
        migrations.AlterField(
            model_name='group',
            name='quantity_of_students',
            field=models.PositiveIntegerField(),
        ),
        migrations.RunPython(forward),
    ]

