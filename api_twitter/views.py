from django.http.response import JsonResponse

from api_twitter.models import Country
from api_twitter.serializers import CountrySerializer
from django.views.decorators.csrf import csrf_exempt




def countries_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        countries_serializer = CountrySerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)


# def filters(request):
#     if request.method == 'GET':
#         countries = Country.objects.filter(code ='EC')
#         countries_serializer = CountrySerializer(countries, many=True)
#         return JsonResponse(countries_serializer.data, safe=False)
    