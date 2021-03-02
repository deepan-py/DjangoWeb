from rest_framework import serializers
from .models import countries

class CountriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = countries
        fields = ('id','name','capital')