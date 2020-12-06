from django.http.response import JsonResponse

from api_twitter.models import *
from api_twitter.serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from http import HTTPStatus
from api_twitter.tweet import *
from api_twitter.analysis import get_analysis
import json



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

        # if filtro_data.get('fecha_inicio') =='':
        #     filtro_data['fecha_inicio']=None
        # if filtro_data.get('fecha_fin') =='':
        #     filtro_data['fecha_fin']=None

        filtro_serializer = FiltroSerializer(data=filtro_data)
        if filtro_serializer.is_valid():
            filtro_serializer.save()
            get_format_filter(filtro_data)
            print(filtro_data)
            tweets = get_tweets_from_tweepy(**filtro_data)
            # print(tweets)
            print('Obtecion de tweet....ok')

            #Analysis
            df_tweets = get_DataFrame(tweets)

            if df_tweets is None:
                return JsonResponse([], status=HTTPStatus.CREATED, safe=False)

            analysis = get_analysis(df_tweets)
            print('Analisis de tweet....ok')


            data = {
                'tweets': df_tweets.reset_index().astype(str).to_dict('records'),
                'analysis':analysis
            }

            return JsonResponse([data], status=HTTPStatus.CREATED, safe=False)
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
""" 

@api_view(['GET', 'POST', 'DELETE'])
def id_list(request):
    if request.method == 'GET':
        ids = Id_Search.objects.all()
        
        title = request.query_params.get('title', None)
        if title is not None:
            ids = ids.filter(title__icontains=title)
        
        ids_serializer = IdSerializer(ids, many=True)
        return JsonResponse(ids_serializer.data, safe=False)
        # 'safe=False' for objects serialization
 
    elif request.method == 'POST':
        id_data = JSONParser().parse(request)
        id_serializer = IdSerializer(data=id_data)
        if id_serializer.is_valid():
            id_serializer.save()
            return JsonResponse(id_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(id_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Id_Search.objects.all().delete()
        return JsonResponse({'message': '{} Id_Searchs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
  """
@csrf_exempt
def id_detail(request):
    
    if request.method == 'GET': 
        ids = Id_Search.objects.all()
        id_serializer = IdSerializer(ids, many=True) 
        return JsonResponse(id_serializer.data, safe=False) 

    elif request.method == 'POST':
        id_data = JSONParser().parse(request)
        id_serializer = IdSerializer(data=id_data)
        if id_serializer.is_valid():
            id_serializer.save()
            return JsonResponse(id_serializer.data, status=HTTPStatus.CREATED) 
        return JsonResponse(id_serializer.errors, status=HTTPStatus.BAD_REQUEST)
 
    elif request.method == 'PUT': 
        id_data = JSONParser().parse(request) 
        id_serializer = IdSerializer(id, data=id_data) 
        if id_serializer.is_valid(): 
            id_serializer.save() 
            return JsonResponse(id_serializer.data) 
        return JsonResponse(id_serializer.errors, status=HTTPStatus.BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        id.delete() 
        return JsonResponse({'message': 'Id_Search was deleted successfully!'}, status=HTTPStatus.BAD_REQUEST)
    
"""        
@api_view(['GET'])
def id_list_published(request):
    ids = Id_Search.objects.filter(published=True)
        
    if request.method == 'GET': 
        ids_serializer = IdSerializer(ids, many=True)
        return JsonResponse(ids_serializer.data, safe=False) """