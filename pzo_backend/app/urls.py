from django.urls import path
from app.views import (
    UserRate,
    GetReportStates,
    GetReportTypes,
    UserData,
    ResetTestData,
    ReportView,
    AcceptReport
)
from app.views import DeleteReport

app_name = "app"

urlpatterns = [
    path("user/", UserData.as_view()),
    path("test/", ResetTestData.as_view()),
    path("user/rate/", UserRate.as_view()),
    path("report/states/", GetReportStates.as_view()),
    path("report/types/", GetReportTypes.as_view()),
    path("reports/", ReportView.as_view(), name="reports"),
    path("reports/<int:pk>/", DeleteReport.as_view()),
    path("reports/accept_report/<int:pk>/", AcceptReport.as_view()),

]
