from django.urls import path
from .views import SignupApiView, CustomAuthToken, CustomDiscardAuthToken
from rest_framework_simplejwt import views as jwt_views

urlpatterns = [
    path('signup/',SignupApiView.as_view()),
    path("api-token-auth/", CustomAuthToken.as_view(), name="api-token-auth"),
    path("logout/", CustomDiscardAuthToken.as_view(), name="token-delete"),
    path(
        "token/create/jwt/",
        jwt_views.TokenObtainPairView.as_view(),
        name="create-jwt",
    ),
    path(
        "token/refresh/jwt/",
        jwt_views.TokenRefreshView.as_view(),
        name="refresh-jwt",
    ),
    path(
        "token/verify/jwt/", jwt_views.TokenVerifyView.as_view(), name="verify-jwt"
    ),
] 
