# Generated by Django 4.2.4 on 2023-12-05 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0011_exam_questions'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='active_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]