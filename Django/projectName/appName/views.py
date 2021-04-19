from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from .models import countries
from .serializers import CountriesSerializer
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET','POST'])
def countries_list(request):
    if request.method == 'GET':
        countries_ = countries.objects.all()
        name = request.GET.get('name',None)
        if name is not None:
            countries_ = countries_.filter(name__icontains=name)
        countries_serializer = CountriesSerializer(countries_,many=True)
        return JsonResponse(countries_serializer.data,safe=False)
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data,status=status.HTTP_201_CREATED)
        return JsonResponse(countries_serializer.errors,status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST','DELETE'])
def countries_detail(request,pk):
    try:
        countries_ = countries.objects.get(pk=pk)
    except countries.DoesNotExist:
        return JsonResponse({'message':'The country doesnt exist'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        countries_serializer = CountriesSerializer(countries_)
        return JsonResponse(countries_serializer.data)
    elif request.method == 'POST':
        countries_data = JSONParser().parse(request)
        countries_serializer = CountriesSerializer(countries_,data=countries_data)
        if countries_serializer.is_valid():
            countries_serializer.save()
            return JsonResponse(countries_serializer.data)
        return JsonResponse(countries_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        countries_.delete()
        return JsonResponse({'message':'Country was deleted successfully'},status=status.HTTP_204_NO_CONTENT)