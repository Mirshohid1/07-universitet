from django.db import models
from django.db.models import SET_NULL


class Faculty(models.Model):
    name = models.CharField(max_length=255)

    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField()

    def __str__(self):
        return self.name

class Student(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    group = models.ForeignKey('Group', related_name='group', on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Kafedra(models.Model):
    name = models.CharField(max_length=255)
    faculty = models.ForeignKey(Faculty, related_name='faculty', on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=255)
    kafedra = models.OneToOneField(Kafedra, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    bio = models.TextField()
    kafedra = models.ForeignKey(Kafedra, on_delete=SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return f"{self.first_name} {self.first_name}"

class Group(models.Model):
    name = models.CharField(max_length=255)
    kafedra = models.OneToOneField(Kafedra, on_delete=SET_NULL, null=True, blank=True)
    teacher = models.ForeignKey(Teacher, on_delete=SET_NULL, null=True, blank=True)
    subject = models.ForeignKey(Subject, on_delete=SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name