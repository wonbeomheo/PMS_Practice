from django.db import models
from django.utils import timezone


# User Model
class User(models.Model):
    CEO = 0
    DEV = 1
    DESIGN = 2
    DATA = 3
    TEAM_CHOICES = [
        (CEO, 'CEO'),
        (DEV, 'Development'),
        (DESIGN, 'Design'),
        (DATA, 'Data'),
    ]
    name = models.CharField(max_length=200)
    team = models.SmallIntegerField(choices=TEAM_CHOICES)

    def __str__(self):
        return self.name


# Project Model
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    start_date = models.DateTimeField('date to start')
    deadline_date = models.DateTimeField('date to finish')

    def __str__(self):
        return self.title


class Task(models.Model):
    IN_PROGRESS = 0
    DONE = 1
    DELAYED = 2
    STATUS_CHOICES = [
        (IN_PROGRESS, 'in progress'),
        (DONE, 'done'),
        (DELAYED, 'delayed'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    detail = models.CharField(max_length=500)
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES,
        default=IN_PROGRESS,
    )
    start_date = models.DateTimeField('date to start')
    deadline_date = models.DateTimeField('date to finish')

    def __str__(self):
        return self.title
