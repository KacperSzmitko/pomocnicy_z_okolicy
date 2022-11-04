from django.contrib import admin
from django.urls import path, include
from app.views import UserRate

urlpatterns = [
    path("admin/", admin.site.urls),
    path("auth/", include("authorization.urls", "authorization")),
    path("user/rate", UserRate.as_view()),

]
