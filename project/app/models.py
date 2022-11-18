from django.db import models
from django.conf import settings
from django.urls import reverse

class Gender(models.Model):
    gendername = models.CharField(max_length=4)

    def __str__(self):
        return self.gendername[:50]

class Groups(models.Model):
    groupname = models.CharField(max_length=25)

    def __str__(self):
        return self.groupname[:50]

class Orphans(models.Model):
    id = models.AutoField(primary_key=True)
    icon = models.ImageField(blank=True)
    name = models.CharField(max_length=255)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE, null=True)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE, null=True)
    dateofbirth = models.DateField(null=True)
    placeofbirth = models.CharField(max_length=255)
    orphan = models.BooleanField(default=False)
    expelled = models.BooleanField(default=False)
    disable = models.BooleanField(default=False)
    dateofreceipt = models.DateField(null=True)
    dateofdeduction = models.DateField(null=True)
    diagnostics = models.CharField(max_length=255, blank=True)
    featuresdiagnostics = models.CharField(max_length=255, blank=True)
    riskgroup = models.CharField(max_length=255, blank=True)


    def __str__(self):
        return self.name[:50]





