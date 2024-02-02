from rest_framework import serializers
from .models import *

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = '__all__'
        
class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = '__all__'  
class TechtoolsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Techtools
        fields = '__all__'        
        
class FilmstarinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filmstarinfo
        fields = '__all__'               
        
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = '__all__'        
 