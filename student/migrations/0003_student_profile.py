# Generated by Django 5.0.1 on 2024-02-03 09:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student", "0002_student_trainer"),
    ]

    operations = [
        migrations.AddField(
            model_name="student",
            name="profile",
            field=models.ImageField(null=True, upload_to="students_profile/"),
        ),
    ]
