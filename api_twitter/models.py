from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=40, blank=False)
    bounding_boxes = models.CharField(max_length=300, blank=False)


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=False)
    username = models.CharField(max_length=80, blank=False)
    texto = models.CharField(max_length=150, blank=False)
    num_mencions = models.IntegerField(default=0)
    num_hashtags = models.IntegerField(default=0)
    longuitud = models.IntegerField(default=0)
    country = models.CharField(max_length=40, blank=False)


class Filtro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(auto_now=False, null=True)
    fecha_fin = models.DateTimeField(auto_now=False, null=True)
    hashtag = models.CharField(max_length=100, null=True)
    num_hashtags = models.IntegerField(default=0)
    mencions = models.CharField(max_length=100, null=True)
    num_mencions = models.IntegerField(default=0)
    keywords = models.CharField(max_length=150, null=True)
    username = models.CharField(max_length=150, null=True)
    fecha_min_creation_user = models.DateTimeField(auto_now=False, null=True)
    fecha_max_creation_user = models.DateTimeField(auto_now=False, null=True)
    username_mencion = models.CharField(max_length=150, null=True)
    min_followers = models.IntegerField(default=0)
    min_friends = models.IntegerField(default=0)
    country = models.CharField(max_length=40, null=True)
    
    len_min_tweet = models.IntegerField(default=0)
    min_faves = models.IntegerField(default=0)
    min_retweets = models.IntegerField(default=0)
    min_replies = models.IntegerField(default=0)
    from_count = models.CharField(max_length=150, null=True)
    language = models.CharField(max_length=10, null=True)


