# Generated by Django 4.2.4 on 2023-09-17 08:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0002_exam_created_at_exam_modified_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exam',
            old_name='end',
            new_name='duration',
        ),
        migrations.RemoveField(
            model_name='exam',
            name='start',
        ),
    ]
