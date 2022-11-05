from django.urls import path
from app.views import UserRate, GetReportStates, GetReportTypes, UserData, ResetTestData

app_name = "app"

urlpatterns = [
    path("user/", UserData.as_view()),
    path("test/", ResetTestData.as_view()),
    path("user/rate", UserRate.as_view()),
    path("report/states", GetReportStates.as_view()),
    path("report/types", GetReportTypes.as_view()),
]

