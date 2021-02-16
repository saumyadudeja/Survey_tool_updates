# Generated by Django 3.1.1 on 2020-10-25 18:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=500, verbose_name='TEXT')),
                ('required', models.BooleanField(default=False)),
                ('image', models.ImageField(upload_to='')),
                ('type', models.CharField(choices=[('text', 'Text'), ('single_choice', 'Single Choice'), ('date', 'Date'), ('multiple_choice', 'Multiple Choice'), ('stated_preference', 'Stated Preference')], default=models.CharField(max_length=500, verbose_name='TEXT'), max_length=200)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polling_app.category')),
            ],
        ),
        migrations.CreateModel(
            name='Respondent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=50)),
                ('age', models.IntegerField()),
                ('gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('diverse', 'Diverse')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Survey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('isPublished', models.BooleanField(verbose_name='Published?')),
                ('publishDate', models.DateTimeField(verbose_name='publication date')),
                ('expiryDate', models.DateTimeField(verbose_name='expiry date')),
            ],
        ),
        migrations.CreateModel(
            name='SurveyQuestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='question_no', to='polling_app.question')),
                ('survey', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polling_app.survey')),
            ],
        ),
        migrations.CreateModel(
            name='Response',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_id', models.CharField(max_length=32)),
                ('respondent', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='polling_app.respondent')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling_app.survey')),
            ],
        ),
        migrations.CreateModel(
            name='AnswerOptions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('option', models.CharField(max_length=200)),
                ('key_name', models.CharField(max_length=200)),
                ('value', models.CharField(max_length=200)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling_app.question')),
            ],
        ),
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.CharField(max_length=20)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling_app.question')),
                ('response', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='polling_app.response')),
            ],
        ),
    ]
