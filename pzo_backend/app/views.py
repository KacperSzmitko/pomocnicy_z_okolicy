from django.shortcuts import render
from rest_framework.views import APIView 
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer, IntegerField, StringRelatedField
from rest_framework.response import Response

from app.models import UsersData, ReportTypes, ReportStates


class UserRate(UpdateAPIView):
    class InputSerializer(ModelSerializer):
        class Meta:
            model = UsersData
            fields = ("points",)

    class OutputSerializer(ModelSerializer):
        class Meta:
            model = UsersData
            fields = ("user", "firstname","surname", "age", "city", "points",)
    

    queryset = UsersData.objects.all()
    serializer_class = InputSerializer

            
    def update(self, request, *args, **kwargs):
        instance:UsersData = UsersData.objects.get(user=request.user)
        instance.points += request.data.get("points")
        instance.save()

        return Response(self.OutputSerializer(instance).data)


class GetReportTypes(ListAPIView):
    class OutputSerializer(ModelSerializer):
        class Meta:
            model = ReportTypes
            fields = ("__all__")

    queryset = ReportTypes.objects.all()

    def get(self, request, *args, **kwargs):
        instance:ReportTypes = ReportTypes.objects.get(type_name=request.data.get("type_name"))
        return(self.OutputSerializer(instance, many=True).data)

class GetReportStates(ListAPIView):
    class OutputSerializer(ModelSerializer):
        class Meta:
            model = ReportStates
            fields = ("__all__")

    queryset = ReportStates.objects.all()

    def get(self, request, *args, **kwargs):
        instance:ReportStates = ReportStates.objects.get(type_name=request.data.get("type_name"))
        return(self.OutputSerializer(instance, many=True).data)
    
