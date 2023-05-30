from django.urls import path, include
from rest_framework import routers
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

# router = routers.DefaultRouter()
# router.register(r'users', views.AccountView)

urlpatterns = [
    path('accounts/', views.create_list_view),
    path('accounts/<int:pk>/', views.delete_list_view),
    
    path('auth/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('auth/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    path('follow/', views.create_follow_list_view),
    path('follow/<int:pk>/', views.delete_follow_list_view),
]