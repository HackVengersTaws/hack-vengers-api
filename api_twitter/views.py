from django.http.response import JsonResponse

from api_twitter.models import *
from api_twitter.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from http import HTTPStatus




def countries_list(request):
    if request.method == 'GET':
        countries = Country.objects.all()
        countries_serializer = CountrySerializer(countries, many=True)
        return JsonResponse(countries_serializer.data, safe=False)

@csrf_exempt
def filtros(request):
    if request.method == 'GET':
        filtros = Filtro.objects.all()
        filtros_serializable = FiltroSerializer(filtros, many=True)
        return JsonResponse(filtros_serializable.data, safe=False)
    
    elif request.method == 'POST':
        filtro_data = JSONParser().parse(request)
        filtro_serializer = FiltroSerializer(data=filtro_data)
        if filtro_serializer.is_valid():
            filtro_serializer.save()
            return JsonResponse(filtro_serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(filtro_serializer.errors, status=HTTPStatus.BAD_REQUEST)

@csrf_exempt
def tweet(request):
    if request.method == 'GET':
        tweets = Tweet.objects.all()
        tweets_serializable = TweetSerializer(tweets, many=True)
        return JsonResponse(tweets_serializable.data, safe=False)
    
    elif request.method == 'POST':
        tweet_data = JSONParser().parse(request)
        tweet_serializer = TweetSerializer(data=tweet_data)
        if tweet_serializer.is_valid():
            tweet_serializer.save()
            return JsonResponse(tweet_serializer.data, status=HTTPStatus.CREATED)
        return JsonResponse(tweet_serializer.errors, status=HTTPStatus.BAD_REQUEST)


# def filters(request):
#     if request.method == 'GET':
#         countries = Country.objects.filter(code ='EC')
#         countries_serializer = CountrySerializer(countries, many=True)
#         return JsonResponse(countries_serializer.data, safe=False)
    