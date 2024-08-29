from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from users.apps import UsersConfig
from users.views import UserCreateView, CoursePurchaseCreateAPIView, UserListView

app_name = UsersConfig.name

urlpatterns = [
    path('user/', UserListView.as_view(), name='user'),
    path('token/refresh', TokenRefreshView.as_view(permission_classes=(AllowAny,)), name='token_refresh'),
    path('login/', TokenObtainPairView.as_view(permission_classes=(AllowAny,)), name='login'),
    path('register/', UserCreateView.as_view(), name='register'),
    path("purchase/", CoursePurchaseCreateAPIView.as_view(), name="create_payment"),
]
