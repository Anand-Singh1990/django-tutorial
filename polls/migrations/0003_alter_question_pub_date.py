# Generated by Django 4.1.5 on 2023-01-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_rename_question_question_question_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='pub_date',
            field=models.DateTimeField(verbose_name='Date Published'),
        ),
    ]
