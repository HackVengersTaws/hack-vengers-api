from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=40, blank=False, default='---')
    bounding_boxes = models.CharField(max_length=300, blank=False, default='---')


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(blank=True)
    username = models.CharField(max_length=80, blank=False, default='---')
    texto = models.CharField(max_length=150, blank=False, default='---')
    num_mencions = models.IntegerField()
    num_hashtags = models.IntegerField()
    longuitud = models.IntegerField()
    country = models.CharField(max_length=40, blank=False, default='---')


class Filtro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(blank=True)
    fecha_fin = models.DateTimeField(blank=True)
    hashtag = models.CharField(max_length=100, blank=False, default='---')
    num_hashtags = models.IntegerField()
    mencions = models.CharField(max_length=100, blank=False, default='---')
    num_mencions = models.IntegerField()
    keywords = models.CharField(max_length=150, blank=False, default='---')
    username = models.CharField(max_length=150, blank=False, default='---')
    fecha_min_creation_user = models.DateTimeField(blank=True)
    fecha_max_creation_user = models.DateTimeField(blank=True)
    username_mencion = models.CharField(max_length=150, blank=False, default='---')
    min_followers = models.IntegerField()
    min_friends = models.IntegerField()
    country = models.CharField(max_length=40, blank=False, default='---')
    len_min_tweet = models.IntegerField()
