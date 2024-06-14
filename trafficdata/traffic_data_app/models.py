from django.db import models
from datetime import datetime

class TrafficData(models.Model):
    id = models.IntegerField(primary_key=True)
    sectionID = models.IntegerField()
    highway = models.IntegerField()
    section = models.IntegerField()
    sectionLength = models.FloatField()
    sectionDescription = models.CharField(max_length=255)
    date = models.DateTimeField(default=datetime.now)
    description = models.CharField(max_length=255)
    group = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    county = models.CharField(max_length=255)
    # ptrucks = models.IntegerField()
    adt = models.IntegerField()
    # aadt = models.CharField(max_length=255)
    direction = models.CharField(max_length=255)
    # pct85 = models.CharField(max_length=255)
    # priorityPoints = models.CharField(max_length=255)