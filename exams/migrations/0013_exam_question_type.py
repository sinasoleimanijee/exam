# Generated by Django 4.2.4 on 2023-12-06 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0012_exam_active_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='exam',
            name='question_type',
            field=models.CharField(choices=[('R', 'READY'), ('A', 'ACTIVE'), ('E', 'EXPIRE')], default='R', max_length=2),
        ),
    ]
