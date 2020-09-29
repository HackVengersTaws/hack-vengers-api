from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=40, blank=False, default='---')
    bounding_boxes = models.CharField(max_length=300, blank=False, default='---')
