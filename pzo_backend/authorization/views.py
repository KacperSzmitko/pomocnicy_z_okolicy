from datetime import datetime
from rest_framework.views import APIView
from django.conf import settings
from authorization.models import User
from rest_framework_simplejwt.tokens import RefreshToken, AccessToken
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenError,
)


def set_tokens_cookies(
    response: Response,
    user: User = None,
    access_expires: int = settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].total_seconds(),
    refresh_expires: int = settings.SIMPLE_JWT[
        "REFRESH_TOKEN_LIFETIME"
    ].total_seconds(),
    *args,
    **kwargs,
):
    """Store tokens in cookies to perist user login

    Args:
        response (Response): Prepared response from view
        access_expires (int, optional): How long to store access token in cookies in seconds. Defaults to settings.SIMPLE_JWT["ACCESS_TOKEN_LIFETIME"].seconds.
        refresh_expires (int, optional): How long to store refresh token in cookies in seconds. Defaults to settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].seconds.
        user (int, optional): If passed last_login field of user will be set to now
    """
    response.set_cookie(
        settings.SIMPLE_JWT["AUTH_COOKIE"],
        response.data["access"],
        max_age=access_expires,
        expires=access_expires,
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )
    response.set_cookie(
        settings.SIMPLE_JWT["REFRESH_COOKIE"],
        response.data["refresh"],
        max_age=refresh_expires,
        expires=refresh_expires,
        httponly=settings.SIMPLE_JWT["AUTH_COOKIE_HTTP_ONLY"],
        samesite=settings.SIMPLE_JWT["AUTH_COOKIE_SAMESITE"],
    )
    if user:
        # user.last_login = datetime.now()
        user.save()
    return response


class TokenObtainPair(TokenObtainPairView):
    def post(self, request: Request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return set_tokens_cookies(
            response, User.objects.get(email=request.data["email"])
        )


class TokenRefresh(TokenRefreshView):
    def post(self, request: Request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        return set_tokens_cookies(
            response, User.objects.get(email=request.data["email"])
        )


class Logout(APIView):
    def post(self, request: Request, *args, **kwargs):
        response = Response(status=200)
        response.delete_cookie("access", samesite="Lax")
        response.delete_cookie("refresh", samesite="Lax")
        return response


class RefreshCookieToken(APIView):
    def get(self, request: Request, *args, **kwargs):
        refresh = request.COOKIES.get("refresh", "")
        if refresh:
            token = RefreshToken(refresh)
            try:
                token.check_exp()
            except TokenError as e:
                return Response(status=401)
            user = User.objects.get(pk=token["user_id"])
            refresh = RefreshToken.for_user(user)
            response = Response(
                data={
                    "refresh": str(refresh),
                    "access": str(refresh.access_token),
                }
            )
            return set_tokens_cookies(response, user)
        return Response(status=401)
