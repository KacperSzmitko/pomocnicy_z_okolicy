from datetime import datetime
from django.db import models
from authorization.models import User
from django.core import validators


class UsersData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(validators=[validators.MinValueValidator(0)])
    city = models.CharField(max_length=255)
    points = models.IntegerField(default=0)
    firstname = models.CharField(max_length=255, default="")
    surname = models.CharField(max_length=255, default="")


class ReportTypes(models.Model):
    type_name = models.CharField(max_length=63)
    lifespan = models.IntegerField(default=3600)


class ReportStates(models.Model):
    state_name = models.CharField(max_length=63)


class Reports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportTypes, on_delete=models.CASCADE)
    report_state = models.ForeignKey(ReportStates, on_delete=models.CASCADE)
    latitude = models.FloatField()
    altitude = models.FloatField()
    time = models.DateTimeField(auto_now_add=True)
    max_people = models.IntegerField(
        validators=[validators.MinValueValidator(1), validators.MaxValueValidator(999)],
        null=True,
        default=None,
    )
    current_people = models.IntegerField(
        validators=[validators.MinValueValidator(0), validators.MaxValueValidator(999)],
        null=True,
        default=0,
    )
    description = models.CharField(max_length=255, null=True, default=None)


class ReportTypesToAccept(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    report_type = models.ForeignKey(ReportTypes, on_delete=models.CASCADE)
