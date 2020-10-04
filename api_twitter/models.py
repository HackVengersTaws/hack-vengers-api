from django.db import models

class Country(models.Model):
    code = models.CharField(max_length=2, primary_key=True)
    name = models.CharField(max_length=40, blank=False)
    bounding_boxes = models.CharField(max_length=300, blank=False)


class Tweet(models.Model):
    id = models.AutoField(primary_key=True)
    fecha = models.DateTimeField(auto_now=False)
    texto = models.CharField(max_length=150, blank=False)
    longuitud = models.IntegerField(default=0)
    hashtags = models.CharField(max_length=250, blank=False)
    num_hashtags = models.IntegerField(default=0)
    mencions = models.CharField(max_length=250, blank=False)
    num_mencions = models.IntegerField(default=0)
    language = models.CharField(max_length=3, blank=False)
    retweet_count = models.IntegerField(default=0)
    favorite_count = models.IntegerField(default=0)
    name_place = models.CharField(max_length=250, blank=False)
    full_name_place = models.CharField(max_length=300, blank=False)
    country = models.CharField(max_length=80, blank=False)
    username = models.CharField(max_length=80, blank=False)
    followers = models.IntegerField(default=0)
    friends = models.IntegerField(default=0)
    create_count = models.DateTimeField(auto_now=False)


class Filtro(models.Model):
    id = models.AutoField(primary_key=True)
    fecha_inicio = models.DateTimeField(auto_now=False, null=True, blank=True)
    fecha_fin = models.DateTimeField(auto_now=False, null=True, blank=True)
    hashtags = models.CharField(max_length=100, null=True, blank=True)
    min_hashtags = models.IntegerField(default=0) #
    mencions = models.CharField(max_length=100, null=True, blank=True)
    min_mencions = models.IntegerField(default=0) #
    keywords = models.CharField(max_length=150, null=True, blank=True)
    username = models.CharField(max_length=150, null=True, blank=True)
    fecha_min_creation_user = models.DateTimeField(auto_now=False, null=True, blank=True) #
    fecha_max_creation_user = models.DateTimeField(auto_now=False, null=True, blank=True) #
    min_followers = models.IntegerField(default=0)#
    min_friends = models.IntegerField(default=0)#
    country = models.CharField(max_length=40, null=True, blank=True)
    len_min_tweet = models.IntegerField(default=0)
    min_faves = models.IntegerField(default=0)
    min_retweets = models.IntegerField(default=0)
    min_replies = models.IntegerField(default=0)
    language = models.CharField(max_length=10, null=True, blank=True)


