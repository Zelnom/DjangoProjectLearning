# Generated by Django 5.0.1 on 2024-01-21 12:44

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0001_initial"),
        ("trainer", "0002_alter_trainer_course"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="trainer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="trainer.trainer",
            ),
        ),
    ]
