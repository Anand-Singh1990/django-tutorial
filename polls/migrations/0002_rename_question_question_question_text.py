# Generated by Django 4.1.5 on 2023-01-31 06:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='Question',
            new_name='question_text',
        ),
    ]
