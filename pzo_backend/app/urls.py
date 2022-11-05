from django.urls import path
from app.views import UserRate, GetReportStates, GetReportTypes

urlpatterns = [
    path("user/rate", UserRate.as_view()),
    path("report/states", GetReportStates.as_view()),
    path("report/types", GetReportTypes.as_view()),
]
