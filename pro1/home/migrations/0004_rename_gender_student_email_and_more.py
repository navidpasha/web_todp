# Generated by Django 4.2.7 on 2023-12-05 12:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_student_delete_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='gender',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='skill',
            new_name='password',
        ),
        migrations.RemoveField(
            model_name='student',
            name='age',
        ),
    ]
