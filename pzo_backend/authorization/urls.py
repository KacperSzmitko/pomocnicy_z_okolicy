from authorization.views import (
    Logout,
    TokenObtainPair,
    TokenRefresh,
    RefreshCookieToken,
)
from django.urls import path, include

app_name = "authorization"

token_patterns = [
    path("", TokenObtainPair.as_view(), name="token_obtain_pair"),
    path("refresh/", TokenRefresh.as_view(), name="token_refresh"),
    path("refresh_cookie/", RefreshCookieToken.as_view(), name="token_cookie_refresh"),
]

urlpatterns = [
    path("token/", include(token_patterns)),
    path("logout/", Logout.as_view()),
]
