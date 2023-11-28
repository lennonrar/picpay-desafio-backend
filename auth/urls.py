from django.urls import path
from auth.views.auth_token import CustomAuthToken
from auth.views.user import UserListCreateView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
app_name = 'auth'

urlpatterns = [
    # path('token/', CustomAuthToken.as_view()),
    path('user/', UserListCreateView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ]