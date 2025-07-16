from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from omnifyApp.serializers import *
from django.utils import timezone


class FitnessAPIView(APIView):

    # Fitness classes creation 
    def post(self,request):
        serializer = FitnessSerializer(data=request.data)
        if serializer.is_valid():
                create = serializer.save()  
                context = {
                    'message': "Fitness classes created successfully",
                    'status_code': 200,
                    'data':serializer.data
                }
                return Response({"results": context})
        
        else:
            return Response({
                "results": {
                    "status_code": 400,
                    "message": 'Bad request.',
                    "errors": serializer.errors
                }
            })

    # Returns a list of all upcoming fitness classes
    def get(self,request):
        today = timezone.localtime(timezone.now())
        data= Fitness.objects.filter(date__gt=today).order_by('-id')
        serializer_class=FitnessSerializer(data,many=True)

        context={'message':"Success",
                 'status_code': 200,
                 "data":serializer_class.data} 
        return Response({"results":context})
    

class BookingAPIView(APIView):

    # Client booking
    def post(self,request):
        fitness = request.data.get("fitness")
        serializer = BookingSerializer(data=request.data)
        if serializer.is_valid():
            create = serializer.save(fitness_id=fitness) 
            updated= Fitness.objects.filter(id=create.fitness.id).first()
            if updated:
                updated.slot = int(updated.slot)-1
                updated.save()
                context = {
                    'message': "Booking successful!",
                    'status_code': 200,
                    'data':serializer.data
                }
                return Response({"results": context})
        
        else:
            return Response({
                "results": {
                    "status_code": 400,
                    "message": 'Bad request.',
                    "errors": serializer.errors
                }
            })
        
    # Returns all bookings made by a specific email address
    def get(self,request):
        email=request.query_params.get('email')
        if email:
            data=Book.objects.filter(client_email=email).order_by('-id')  
            serializer= BookingSerializer(data,many=True)
            context={'message':"Success",
                 'status_code': 200,
                 "data":serializer.data} 
            return Response({"results":context})
        else:
            context = {
                'message': "Email query param is required.",
                'status_code': 400,
                "data": []
            }
            return Response({"results": context})
