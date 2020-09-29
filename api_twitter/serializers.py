from rest_framework import serializers 
from api_twitter.models import Country


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Country
        fields = ('code',
                  'name'
                  )





def load_data():
    from api_twitter.country_bounding_boxes import get_country_bounding_boxes

    country_bounding_boxes = get_country_bounding_boxes()
    for code, data in country_bounding_boxes.items():
        country = Country.objects.create(code=code, name=data[0], bounding_boxes=data[1])
        country.save()
    print("Paises cargadas....OK")



# load_data()