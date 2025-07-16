from django.urls import path, include
from django.contrib.auth import get_user_model
from rest_framework import routers, serializers, viewsets, fields
from omnifyApp.models import *

# Serializer for the Fitness model
class FitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = '__all__'

    #validation for fitness model fields
    def validate(self, data):

        required_fields = ["name", "type", "date", "instructor", "slot"]
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: "This field is required"})
              
        if "slot" in data:
            if not str(data["slot"]).isdigit():
                raise serializers.ValidationError("Enter a valid slot number")
        return data


# Serializer for the Book model
class BookingSerializer(serializers.ModelSerializer):
    class_id= serializers.SerializerMethodField()
    class Meta:
        model = Book
        fields = ['id','class_id','client_name','client_email']
    
    def get_class_id(self, obj):
        return obj.fitness.id if obj.fitness else None
    
    #validation for book model fields
    def validate(self, data):
        required_fields = ['client_name','client_email']
        for field in required_fields:
            if field not in data or data[field] is None:
                raise serializers.ValidationError({field: "This field is required"})
              
        fitness_id = self.initial_data.get('fitness')
        if not fitness_id:
            raise serializers.ValidationError({"class_id": "This field is required"})
        
        if 'fitness' in self.initial_data:
            value=Fitness.objects.filter(id=self.initial_data.get('fitness')).first()
            if value.slot==None or int(value.slot)<=0:
                 raise serializers.ValidationError("Slots are not available")
        return data
            
        