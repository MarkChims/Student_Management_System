from django.db import models


# Create your models here.
class Student(models.Model):
    first_name = models.Charfield(max_length=30)
    last_name = models.Charfield(max_length=30)
    gender = models.CharField(max_length=6, default="Male")
    contact = models.EmailField()
    profile_image = models.ImageField(default="user.jpeg", blank=True)
    reg_number = models.CharField(max_length=8)
    level = models.ForeignKey(Level, related_name="students", on_delete=models.CASCADE)
    password = models.CharField(max_length=16)


class Admin(models.Model):
    admin_id = models.CharField(max_length=8)
    first_name = models.Charfield(max_length=30)
    last_name = models.Charfield(max_length=30)
    gender = models.CharField(max_length=6, default="Male")
    contact = models.EmailField()
    password = models.CharField(max_length=16, unique=True)
    profile_image = models.ImageField(default="user.jpeg", blank=True)


class Dormitory(models.Model):
    code = models.Charfield(max_length=3, unique=True)
    name = models.CharField(max_length=10)
    status = models.BooleanField(default=False)
    capacity = models.SmallIntegerField(default=30)
    dorm_image = models.ImageField(default="hostels.jpg")


class Room(models.Model):
    code = models.CharField(max_length=2, unique=True)
    name = models.CharField(max_length=50)
    capacity = models.SmallIntegerField(default=1)
    status = models.BooleanField(default=False)
    dorm = models.ForeignKey(
        Dormitory, related_name="dorm-room", on_delete=models.CASCADE
    )


class Residence(models.Model):
    room = models.ForeignKey(Room, related_name="residences", on_delete=models.CASCADE)
    student = models.ForeignKey(
        Student, related_name="residences", on_delete=models.CASCADE
    )
    date = models.DateTimeField(auto_now=True, auto_now_add=False)


class Level(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)


class Subject(models.Model):
    code = models.CharField(max_length=4, unique=True)
    name = models.CharField(max_length=50)
    level = models.ForeignKey(Level, related_name="subjects", on_delete=models.CASCADE)
    duration = models.SmallIntegerField(default=3)
    methodologies = models.CharField()
