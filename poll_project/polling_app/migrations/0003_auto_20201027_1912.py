# Generated by Django 3.1.1 on 2020-10-27 18:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polling_app', '0002_question_survey'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='category',
        ),
        migrations.RemoveField(
            model_name='question',
            name='survey',
        ),
    ]
