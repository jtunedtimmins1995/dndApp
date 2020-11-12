from django.db import models

# Create your models here.
class captive(models.Model):
    def __str__(self):
        return self.name

    image = models.CharField(max_length=255, default=None, null=True)
    name = models.CharField(max_length=255, default=None, null=True)
    date_of_acquisition = models.CharField(max_length=255, default=None, null=True)
    status = models.CharField(max_length=255, default=None, null=True)
    comments = models.CharField(max_length=255, default=None, null=True)
    batch = models.CharField(max_length=255, default=None, null=True)
    
class statusFlags(models.Model):
    def __str__(self):
        return self.descriptor

    descriptor = models.CharField(max_length=255, unique=True)
    stage = models.CharField(max_length=255, default=None, null=True)

class email(models.Model):
    subject = models.CharField(max_length=255, default=None, null=True)
    to = models.CharField(max_length=255, default=None, null=True)
    cc = models.CharField(max_length=255, default=None, null=True)
    text = models.CharField(max_length=255, default=None, null=True)

    