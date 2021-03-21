from rest_framework import serializers
from .models import *
from django.contrib.auth.models import User


class categorySerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Category
        fields='__all__'


class optionSerializer(serializers.ModelSerializer):

    class Meta:
        model=Options
        fields='__all__'
        


   

class testSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=Test
        fields='__all__'
    

    