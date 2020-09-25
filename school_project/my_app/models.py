from django.db import models
from django.urls import reverse


# Create your models here.
class School(models.Model):
    sch_name = models.CharField(max_length=100)
    sch_principal = models.CharField(max_length=100)
    sch_location = models.CharField(max_length=200)

    def __str__(self):
        return self.sch_name

    def get_absolute_url(self):
        # This method is used whe we create school then after that where we render the page like below code, after
        # create render school_detail page.
        # return reverse('my_app:school_detail', kwargs={'pk': self.pk})
        return reverse('my_app:schools')


class Student(models.Model):
    stu_name = models.CharField(max_length=100)
    stu_age = models.PositiveIntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.stu_name
