# Generated by Django 4.2.4 on 2024-08-07 06:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exams', '0025_alter_exam_exam_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exam',
            name='exam_date',
            field=models.CharField(default='1403/05/17', max_length=20, verbose_name='Persian Datetime'),
        ),
    ]