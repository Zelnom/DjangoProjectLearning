from django.db import models


class Trainer(models.Model):

    department_options = (
        ("frontend", "Frontend"),
        ("backend", "Backend"),
        ("network", "Network"),
    )
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    course = models.CharField(max_length=40, blank=True, null=True)
    email = models.EmailField(max_length=40)
    department = models.CharField(max_length=32, choices=department_options)
    active = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    image_up = models.ImageField(upload_to="trainers_images/", null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    def delete(self, *args, **kwargs):
        self.active = False
        return super().save(*args, **kwargs)


class Course(models.Model):
    name = models.CharField(max_length=40)
    trainer = models.CharField(max_length=40)
    description = models.TextField(max_length=400)

    def __str__(self):
        return self.name
