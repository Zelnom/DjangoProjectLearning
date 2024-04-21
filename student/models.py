from django.contrib.auth.models import User
from django.db import models

from trainer.models import Trainer


class Student(models.Model):

    gender_options = (
        ("male", "Male"),
        ("female", "Female")
    )

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.IntegerField()
    email = models.EmailField(max_length=60)
    description = models.TextField(max_length=400)
    active = models.BooleanField(default=True)
    gender = models.CharField(max_length=6, choices=gender_options)
    start_date = models.DateField()
    end_start = models.DateField()
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True)
    profile = models.ImageField(upload_to="students_profile/", null=True)

# ce inseamna on_delete=models.CASCADE ...daca alocam un trainer studentului si stergem trainer-ul
# se sterge automat si studentul

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class HistoryStudent(models.Model):
    message = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

