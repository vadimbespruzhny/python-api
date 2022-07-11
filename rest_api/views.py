from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Parameter, User
from .serializers import ParameterSerializer, ParameterItemSerializer, UserSerializer
# Create your views here.


class AllUsersParameterView(APIView):
    def get(self, request, user_name):
        user = User.objects.get(name=user_name)
        user_params = Parameter.objects.filter(user=user)
        serializer = ParameterSerializer(
            user_params, many=True, context={"request": request})
        return Response({"result": serializer.data})

    def post(self, request, user_name):
        user = User.objects.get(name=user_name)
        user_params_list = Parameter.objects.filter(
            user=user).values_list("parameter_name", flat=True)

        if not request.data["parameter_name"] in user_params_list:
            serializer = ParameterSerializer(Parameter(), data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(user=user)
                return Response(serializer.data)
            return Response(serializer.errors)

        return Response({"message": "Такой параметр уже существует"})


class ParameterView(APIView):
    def get(self, request, user_name, parameter_name):
        user = User.objects.get(name=user_name)
        user_params = Parameter.objects.filter(user=user)

        user_params_list = user_params.values_list("parameter_name", flat=True)
        if not parameter_name in user_params_list:
            return Response({"result": []})

        p_name = user_params.get(parameter_name=parameter_name)

        serializer = ParameterItemSerializer(
            p_name, context={"request": request})
        return Response({"result": serializer.data})


class UserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(
            users, many=True, context={"request": request})
        return Response({"users": serializer.data})

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)
