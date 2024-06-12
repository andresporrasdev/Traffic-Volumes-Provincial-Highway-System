from django.db import models

class TrafficData(models.Model):
    sectionID = models.IntegerField()
    highway = models.IntegerField()
    section = models.IntegerField()
    sectionLength = models.FloatField()
    sectionDescription = models.TextField()
    date = models.DateField()
    description = models.TextField()
    group = models.TextField()
    type = models.TextField()
    county = models.TextField()
    ptrucks = models.FloatField()
    adt = models.IntegerField()
    direction = models.TextField()