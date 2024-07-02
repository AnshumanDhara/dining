from rest_framework import serializers
from core.models import User, Place

class DiningSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        
class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']
        
class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'
        
class NameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = 'name'