from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import serializers
from app.models import User, UsersData, Reports, ReportTypes, ReportStates, ReportTypesToAccept
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView 
from rest_framework.generics import UpdateAPIView 
from rest_framework.serializers import ModelSerializer

from pzo_backend.app.models import UsersData
class UserData(APIView):
    class UserDataSerializer(serializers.ModelSerializer):
        email = serializers.SerializerMethodField()

        class Meta:
            model = UsersData
            fields = ("email", "firstname", "surname", "age", "city", "points")
        
        def get_email(self, obj):
            return obj.user.email

    def get(self, request: Request):
        #TODO
        #user_data = UsersData.objects.filter(user=request.user) 
        user_data = UsersData.objects.filter(user=User.objects.first())
        result = self.UserDataSerializer(user_data[0])
        return Response(data=result.data)

class ResetTestData(APIView):
    def get(self, request: Request):

        Reports.objects.all().delete()
        ReportStates.objects.all().delete()
        ReportTypesToAccept.objects.all().delete()
        ReportTypes.objects.all().delete()
        UsersData.objects.all().delete()
        User.objects.all().delete()

        rs_n = ReportStates.objects.create(state_name="NEW")
        rs_a = ReportStates.objects.create(state_name="ACTIVE")
        rs_f = ReportStates.objects.create(state_name="FINISHED")

        rt_i = ReportTypes.objects.create(type_name="INFO", lifespan=1200)
        rt_h = ReportTypes.objects.create(type_name="HELP", lifespan=2400)
        rt_d = ReportTypes.objects.create(type_name="DANGER", lifespan=3600)

        u1 = User.objects.create(email="u1@xd.com")
        u2 = User.objects.create(email="u2@xd.com")
        u3 = User.objects.create(email="u3@xd.com")

        UsersData.objects.create(user=u1, firstname="Marcin", surname="Tajsner", age=3, city="Poznań", points=99999)
        UsersData.objects.create(user=u2, firstname="Kacper", surname="Szmitko", age=87, city="Zielona góra", points=-41)
        UsersData.objects.create(user=u3, firstname="Maciej", surname="Stefaniak", age=12, city="Bydgoszcz", points=2)

        ReportTypesToAccept.objects.create(user=u1, report_type=rt_i)
        ReportTypesToAccept.objects.create(user=u1, report_type=rt_h)
        ReportTypesToAccept.objects.create(user=u1, report_type=rt_d)
        ReportTypesToAccept.objects.create(user=u2, report_type=rt_h)
        ReportTypesToAccept.objects.create(user=u2, report_type=rt_d)
        ReportTypesToAccept.objects.create(user=u3, report_type=rt_i)

        Reports.objects.create(user=u1, report_type=rt_d, report_state=rs_a, latitude=52.40, altitude=16.92, description="Wielki chłop")
        Reports.objects.create(user=u2, report_type=rt_i, report_state=rs_n, latitude=50.33, altitude=16.12, max_people=10, current_people=0, description="Jedzenie za darmo")
        Reports.objects.create(user=u2, report_type=rt_h, report_state=rs_f, latitude=49.11, altitude=14.17, max_people=3, current_people=0, description="Proszę o pomoc w przeniesieniu wersalki")
        
        return Response(status=200)

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

    
