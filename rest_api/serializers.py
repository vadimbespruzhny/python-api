from rest_framework import serializers
from .models import Parameter, User

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ["parameter_name", "parameter_type", "parameter_value"]
        

class ParameterItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['parameter_value', 'parameter_type']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"