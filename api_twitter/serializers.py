from rest_framework import serializers 
from api_twitter.models import *


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('code',
                  'name'
                  )

class TweetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweet
        fields = ('fecha', 
                'texto', 
                'longuitud', 
                'hashtags', 
                'num_hashtags', 
                'mencions', 
                'num_mencions', 
                'language', 
                'retweet_count', 
                'favorite_count', 
                'name_place', 
                'full_name_place', 
                'country', 
                'username', 
                'followers', 
                'friends', 
                'create_count'
                  )

class FiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filtro
        fields = ('id',
                #   'fecha_inicio',
                #   'fecha_fin',
                  'hashtags',
                  'min_hashtags',
                  'mencions',
                  'min_mencions',
                  'keywords',
                  'username',
                  'fecha_min_creation_user',
                  'fecha_max_creation_user',
                  'min_followers',
                  'min_friends',
                  'len_min_tweet',
                  'country',
                  'len_min_tweet',
                  'min_faves',
                  'min_retweets',
                  'min_replies',
                  'language',
                  )
                  


def load_data():
    from api_twitter.country_bounding_boxes import get_country_bounding_boxes

    country_bounding_boxes = get_country_bounding_boxes()
    for code, data in country_bounding_boxes.items():
        country = Country.objects.create(code=code, name=data[0], bounding_boxes=data[1])
        country.save()
    print("Paises cargadas....OK\n")

# load_data()