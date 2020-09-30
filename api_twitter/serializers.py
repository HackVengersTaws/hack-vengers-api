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
                  'username',
                  'texto',
                  'num_mencions',
                  'num_hashtags',
                  'longuitud',
                  'country'
                  )

class FiltroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filtro
        fields = ('fecha_inicio',
                  'username',
                  'keywords',
                  'num_mencions',
                  'num_hashtags',
                  'len_min_tweet',
                  'country'
                  )


def load_data():
    from api_twitter.country_bounding_boxes import get_country_bounding_boxes

    country_bounding_boxes = get_country_bounding_boxes()
    for code, data in country_bounding_boxes.items():
        country = Country.objects.create(code=code, name=data[0], bounding_boxes=data[1])
        country.save()
    print("Paises cargadas....OK")

# load_data()