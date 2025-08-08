from django.db import models
from django.contrib.auth.models import User
import datetime


# Create your models here.
class Level(models.Model):
    code = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # links to Django User
    reg_number = models.CharField(max_length=8, unique=True)
    gender = models.CharField(max_length=6, default="Male")
    profile_image = models.ImageField(default="user.jpeg", blank=True)
    level = models.ForeignKey(Level, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    


class Admin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # links to Django User
    admin_id = models.CharField(max_length=8, unique=True)
    gender = models.CharField(max_length=6, default="Male")
    profile_image = models.ImageField(default="user.jpeg", blank=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Dormitory(models.Model):
    code = models.CharField(max_length=3, unique=True)
    name = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    capacity = models.SmallIntegerField(default=30)
    floor = models.SmallIntegerField(default=1)
    dorm_image = models.ImageField(default="hostels.jpg")

    def __str__(self):
        return self.name


class Room(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    capacity = models.SmallIntegerField(default=1)
    status = models.BooleanField(default=False)
    dorm = models.ForeignKey(
        Dormitory, related_name="dorm_room", on_delete=models.CASCADE
    )
    floor = models.SmallIntegerField(default=1)

    def __str__(self):
        def txt():
            txt = "st" if self.floor == 1 else "nd" if self.floor == 2 else "rd" if self.floor == 3 else "th"
        return f"{ self.name } "


class Residence(models.Model):
    room = models.ForeignKey(Room, related_name="residences", on_delete=models.CASCADE)
    dorm = models.ForeignKey(Dormitory, related_name="Dorm_Name", on_delete=models.CASCADE, default=1)
    student = models.ForeignKey(
        Student, related_name="student_residences", on_delete=models.CASCADE
    )
    date = models.DateTimeField( auto_now=True)


class Subject(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level, related_name="subjects", on_delete=models.CASCADE)
    duration = models.SmallIntegerField(default=3)
    methodologies = models.CharField()

    def __str__(self):
        return self.name

class Registration(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now=True)

