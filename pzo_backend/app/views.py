from rest_framework.views import APIView
from rest_framework import serializers
from app.models import (
    User,
    UsersData,
    Reports,
    ReportTypes,
    ReportStates,
    ReportTypesToAccept,
)
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import UpdateAPIView, ListAPIView, DestroyAPIView
from rest_framework.serializers import ModelSerializer
from django.db.models import Q
import math
from django.db.models.query import QuerySet


class UserData(APIView):
    class UserDataSerializer(serializers.ModelSerializer):
        email = serializers.SerializerMethodField()

        class Meta:
            model = UsersData
            fields = ("id", "email", "firstname", "surname", "age", "city", "search_area", "points")

        def get_email(self, obj):
            return obj.user.email

    def get(self, request: Request) -> Response:
        # TODO
        # user_data = UsersData.objects.filter(user=request.user)
        user_data = UsersData.objects.filter(user=User.objects.first())
        result = self.UserDataSerializer(user_data[0])
        return Response(data=result.data)


class ResetTestData(APIView):
    def get(self, request: Request) -> Response:

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

        UsersData.objects.create(
            user=u1,
            firstname="Marcin",
            surname="Tajsner",
            age=3,
            city="Poznań",
            search_area=1000,
            points=99999
        )
        UsersData.objects.create(
            user=u2,
            firstname="Kacper",
            surname="Szmitko",
            age=87,
            city="Zielona góra",
            search_area=100,
            points=-41
        )
        UsersData.objects.create(
            user=u3,
            firstname="Maciej",
            surname="Stefaniak",
            age=12,
            city="Bydgoszcz",
            search_area=300,
            points=2
        )

        ReportTypesToAccept.objects.create(user=u1, report_type=rt_i)
        ReportTypesToAccept.objects.create(user=u1, report_type=rt_h)
        ReportTypesToAccept.objects.create(user=u1, report_type=rt_d)
        ReportTypesToAccept.objects.create(user=u2, report_type=rt_h)
        ReportTypesToAccept.objects.create(user=u2, report_type=rt_d)
        ReportTypesToAccept.objects.create(user=u3, report_type=rt_i)

        Reports.objects.create(
            user=u1,
            report_type=rt_d,
            report_state=rs_a,
            latitude=52.40,
            altitude=16.92,
            description="Wielki chłop",
        )
        Reports.objects.create(
            user=u2,
            report_type=rt_i,
            report_state=rs_n,
            latitude=50.33,
            altitude=16.12,
            max_people=10,
            current_people=0,
            description="Jedzenie za darmo",
        )
        Reports.objects.create(
            user=u2,
            report_type=rt_h,
            report_state=rs_f,
            latitude=49.11,
            altitude=14.17,
            max_people=3,
            current_people=0,
            description="Proszę o pomoc w przeniesieniu wersalki",
        )

        return Response(status=200)


class UserRate(UpdateAPIView):
    class InputSerializer(ModelSerializer):
        class Meta:
            model = UsersData
            fields = ("points",)

    class OutputSerializer(ModelSerializer):
        class Meta:
            model = UsersData
            fields = (
                "user",
                "firstname",
                "surname",
                "age",
                "city",
                "search_area",
                "points"
            )

    queryset = UsersData.objects.all()
    serializer_class = InputSerializer

    def update(self, request) -> Response:
        instance: UsersData = UsersData.objects.get(user=request.user)
        instance.points += request.data.get("points")
        instance.save()

        return Response(self.OutputSerializer(instance).data)


class GetReportTypes(ListAPIView):
    class OutputSerializer(ModelSerializer):
        class Meta:
            model = ReportTypes
            fields = "__all__"

    queryset = ReportTypes.objects.all()

    def get(self, request) -> Response:
        instance = ReportTypes.objects.all()
        return Response(data=self.OutputSerializer(instance, many=True).data)


class GetReportStates(ListAPIView):
    class OutputSerializer(ModelSerializer):
        class Meta:
            model = ReportStates
            fields = "__all__"

    queryset = ReportStates.objects.all()

    def get(self, request) -> Response:
        instances = ReportStates.objects.all()
        return Response(data=self.OutputSerializer(instances, many=True).data)


class AcceptReport(APIView):
    def get(self, request: Request, pk: int) -> Response:
        obj = Reports.objects.get(pk=pk)
        if obj.current_people:
            obj.current_people += 1
            obj.save()

        return Response(status=201)


class ReportView(APIView):
    class ReportSerializer(serializers.ModelSerializer):
        class Meta:
            model = Reports
            fields = "__all__"

    def get(self, request: Request) -> Response:
        latitude, longitude = (
            request.query_params.get("latitude", None),
            request.query_params.get("altitude", None)
        )
        if not latitude or not longitude:
            return Response(status=400)

        latitude, longitude = float(latitude), float(longitude)
        # TODO
        # area = float(UsersData.objects.get(user=request.user).search_area)
        area = float(UsersData.objects.get(user=User.objects.first()).search_area)

        earth_r = 6378.137
        pi = math.pi
        m = (1 / ((2 * pi / 360.0) * earth_r)) / 1000.0
        latitude_distance = m * area
        longitude_distance = (m * area) / math.cos(latitude * (pi / 180.0))

        t = ReportTypesToAccept.objects.filter(user=User.objects.first()).values("report_type")

        obj = Reports.objects.filter(
            ~Q(report_state = "FINISHED"),
            # TODO
            #report_type__in = ReportTypesToAccept.objects.filter(user=request.user).values("report_type"),
            report_type__in = ReportTypesToAccept.objects.filter(user=User.objects.first()).values("report_type"),
            latitude__range = (latitude-latitude_distance, latitude+latitude_distance),
            altitude__range = (longitude-longitude_distance, longitude+longitude_distance)
        )
        reports = self.ReportSerializer(obj, many=True)
        return Response(data=reports.data)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def post(self, request: Request) -> Response:

        report = self.ReportSerializer(data=request.data)  # type: ignore
        report.is_valid(raise_exception=True)
        report.save()
        return Response(data=report.data)

class DeleteReport(APIView):
    def get_queryset(self) -> QuerySet:
        return Reports.objects.filter(user=self.request.user)

    def delete(self, request:Request, pk: int) -> Response:
        try:
            self.get_queryset().get(pk=pk).delete()
        except Exception as e:
            return Response(status=404)
        return Response(status=204)
