# Generated by Django 4.2.2 on 2023-06-29 17:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('basics', '0002_alter_student_file'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
    ]
