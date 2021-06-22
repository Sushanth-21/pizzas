from django.db.models import fields
from rest_framework import serializers
from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password
from .models import Toppings, Pizza


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password']

    def create(self, validated_data):
        hashed_pass = make_password(validated_data['password'])
        user = User.objects.create(
            username=validated_data['username'], password=hashed_pass)

        return user


class ToppingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toppings
        fields = ['name']


class PizzaCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pizza
        fields = ['created_by', 'type', 'size']


class PizzaSerializer(serializers.ModelSerializer):
    toppings = ToppingsSerializer(read_only=True, many=True)
    created_by = UserSerializer(read_only=True)

    class Meta:
        model = Pizza
        fields = '__all__'
