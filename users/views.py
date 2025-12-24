from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import FormView
from django.contrib.auth import login
from rest_framework import generics, permissions
from .serializers import RegisterUserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from rest_framework.authentication import TokenAuthentication



# Create your views here.
class RegisterView(FormView):
    '''
    Register a user
    '''
    template_name = ''
    form_class = UserCreationForm
    success_url = '/'

    def form_valid(self, form):
        user = form.save()
        login(self.request, user) # do auto login onregistration
        return redirect(self.get_success_url())
    
    def dispatch(self, request, *args, **kwargs):
        '''
        prevent logged in users from registering again
        '''
        if request.user.is_authenticated:
            return redirect('home')
        return super().dispatch(request, *args, **kwargs)
    

# APIs
@method_decorator(csrf_exempt, name='dispatch')
class RegisterAPIView(generics.CreateAPIView):
    serializer_class = RegisterUserSerializer
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        token, created = Token.objects.get_or_create(user=user)

        user_data = RegisterUserSerializer(user).data
        return Response({
            'user':user_data,
            'token':token.key,
            "message": "User registered successfully"
        }, status=status.HTTP_201_CREATED)


class LoginAPIView(ObtainAuthToken):
    def post(self, request):
        serializer = self.serializer_class(
            data=request.data, 
            context={'request':request}
            )
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']

        token, _ = Token.objects.get_or_create(user=user)
        return Response({
            'user_id':user.id,
            'username':user.username,
            'token':token.key,
            'message':'Logged in successfully'
        }, status=status.HTTP_200_OK)
    

class LogoutAPIView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        request.user.auth_token.delete()
        return Response({
            'detail':'Successfully logged out',
            'message':'User is logged out'
        }, status=status.HTTP_200_OK)