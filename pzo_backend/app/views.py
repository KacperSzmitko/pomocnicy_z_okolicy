from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.generics import UpdateAPIView 
from rest_framework.serializers import ModelSerializer
from rest_framework.response import Response

from pzo_backend.app.models import UsersData

class UserRate(UpdateAPIView):
    class ClientNameSerializer(ModelSerializer):
        class Meta:
            model = UsersData
            fields = ("points",)

    queryset = UsersData.objects.all()

            
    def update(self, request, *args, **kwargs):
        instance:UsersData = UsersData.objects.get(user=request.user)
        instance.points += request.data.get("points")
        instance.save()

        return Response(str(isinstance))

    
