# Generated by Django 5.1.2 on 2024-10-18 04:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_question_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='owner',
        ),
    ]