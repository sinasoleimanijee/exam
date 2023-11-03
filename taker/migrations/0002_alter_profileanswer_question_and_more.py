# Generated by Django 4.2.4 on 2023-11-01 18:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0001_initial'),
        ('questions', '0003_questiongroup_q_bank'),
        ('taker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profileanswer',
            name='question',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='question_prof_answers', related_query_name='question_prof_answer', to='questions.question'),
        ),
        migrations.AlterField(
            model_name='profileanswer',
            name='result',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='result_prof_answers', related_query_name='result_prof_answer', to='result.result'),
        ),
    ]