from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework import status

from accounts.serializers import UserSerializer

from django.db.utils import IntegrityError

class Login(APIView):
    def post(self, request):
        try:
            username = request.data['username']
            password = request.data['password']

            user = authenticate(username=username, password=password)

            if user != None:
                token = Token.objects.get_or_create(user=user)[0]
                return Response({'token': token.key})
            
            return Response({'msg': 'Wrong username or password'}, status=status.HTTP_401_UNAUTHORIZED)
        except KeyError as e:
            return Response({'msg': f'{str(e)} is missing'})


class Register(APIView):
    def post(self, request):
        try:       
            username = request.data['username']
            password = request.data['password']
            is_staff = request.data['is_staff']
            is_superuser = request.data['is_superuser']

            user = User.objects.create_user(username=username, password=password, is_staff=is_staff, is_superuser=is_superuser)
            serializer = UserSerializer(user)
            output = {
                **serializer.data,
                'is_staff': user.is_staff,
                'is_superuser': user.is_superuser
            }

            return Response(output, status=status.HTTP_201_CREATED)
        except IntegrityError:
            return Response({'msg': 'User already exists'}, status=status.HTTP_409_CONFLICT)
