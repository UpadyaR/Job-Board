# Generated by Django 5.1 on 2024-08-09 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job_board', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='jobposting',
            name='is_active',
            field=models.BooleanField(default=False),
        ),
    ]
