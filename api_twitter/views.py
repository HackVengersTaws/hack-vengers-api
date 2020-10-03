from django.http.response import JsonResponse

from api_twitter.models import *
from api_twitter.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from http import HTTPStatus
from api_twitter.tweet import *
from api_twitter.analysis import get_analysis



def get_format_filter(dic_filter):
    '''
    This fuction is used to convert string into a list of strings
    '''
    list_filter = ['hashtags', 'mencions', 'keywords']
    for type_filter in list_filter:
        if type_filter in dic_filter:
            dic_filter[type_filter] = dic_filter[type_filter].split(',')



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
            # filtro_serializer.save()
            get_format_filter(filtro_data)
            print(filtro_data)
            tweets = get_tweets_from_tweepy(**filtro_data)

            #Analysis
            df_tweets = get_DataFrame(tweets)
            analysis = get_analysis(df_tweets)

            data = {
                'tweets': tweets,
                'analysis':analysis
            }

            return JsonResponse(data, status=HTTPStatus.CREATED, safe=False)
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


    