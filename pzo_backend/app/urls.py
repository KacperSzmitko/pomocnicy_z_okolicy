from django.urls import path

from app.views import UserData, ResetTestData

app_name = "app"

urlpatterns = [
    path("user/", UserData.as_view()),
    path("test/", ResetTestData.as_view())
]
