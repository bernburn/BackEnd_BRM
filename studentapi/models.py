from django.db import models

from django.db import models

class Student(models.Model):
    student_id = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=100)
    course = models.CharField(max_length=50)
    year_level = models.IntegerField()

    def __str__(self):
        return f"{self.full_name} ({self.student_id})"