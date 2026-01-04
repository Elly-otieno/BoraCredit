from django.urls import path
from django.contrib.auth import views as auth_views   # django in built auth 
from .views import RegisterView, RegisterAPIView, LoginAPIView, LogoutAPIView, UserProfileAPIView


urlpatterns = [
    # TEMPLATE VIEWS
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(template_name='users/register.html'), name='register'),

    # API VIEWS
    path('api/register/', RegisterAPIView.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/logout/', LogoutAPIView.as_view(), name='logout'),
    path('api/profile/', UserProfileAPIView.as_view(), name='profile'),
]