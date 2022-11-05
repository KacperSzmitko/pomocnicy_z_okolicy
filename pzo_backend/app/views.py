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
from rest_framework.generics import UpdateAPIView, ListAPIView
from rest_framework.serializers import ModelSerializer


class UserData(APIView):
    class UserDataSerializer(serializers.ModelSerializer):
        email = serializers.SerializerMethodField()

        class Meta:
            model = UsersData
            fields = ("email", "firstname", "surname", "age", "city", "points")

        def get_email(self, obj):
            return obj.user.email

    def get(self, request: Request):
        # TODO
        # user_data = UsersData.objects.filter(user=request.user)
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

        UsersData.objects.create(
            user=u1,
            firstname="Marcin",
            surname="Tajsner",
            age=3,
            city="Poznań",
            points=99999,
        )
        UsersData.objects.create(
            user=u2,
            firstname="Kacper",
            surname="Szmitko",
            age=87,
            city="Zielona góra",
            points=-41,
        )
        UsersData.objects.create(
            user=u3,
            firstname="Maciej",
            surname="Stefaniak",
            age=12,
            city="Bydgoszcz",
            points=2,
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
                "points",
            )

    queryset = UsersData.objects.all()
    serializer_class = InputSerializer

    def update(self, request, *args, **kwargs):
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

    def get(self, request, *args, **kwargs):
        instance: ReportTypes = ReportTypes.objects.get(
            type_name=request.data.get("type_name")
        )
        return self.OutputSerializer(instance, many=True).data


class GetReportStates(ListAPIView):
    class OutputSerializer(ModelSerializer):
        class Meta:
            model = ReportStates
            fields = "__all__"

    queryset = ReportStates.objects.all()

    def get(self, request, *args, **kwargs):
        instance: ReportStates = ReportStates.objects.get(
            type_name=request.data.get("type_name")
        )
        return self.OutputSerializer(instance, many=True).data


class ReportView(APIView):
    class ReportSerializer(serializers.ModelSerializer):
        class Meta:
            model = Reports
            fields = "__all__"

    def get(self, request: Request) -> Response:
        latitude, area, altitude = (
            request.query_params.get("latitude", None),
            request.query_params.get("altitude", None),
            request.query_params.get("area", None),
        )
        if not latitude or not area or not altitude:
            return Response(status=400)
        latitude, area, altitude = float(latitude), float(area), float(altitude)
        obj = Reports.objects.filter(
            latitude__range=(latitude - area, latitude + area),
            altitude__range=(altitude - area, altitude + area),
        )
        reports = self.ReportSerializer(obj, many=True)
        return Response(reports.data)

    def post(self, request: Request) -> Response:
        report = self.ReportSerializer(data=request.data)
        report.is_valid(raise_exception=True)
        report.save()
        return Response(report.data)
