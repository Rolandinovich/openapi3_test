import jwt
from django.conf import settings
from django.shortcuts import render

# Create your views here.

# class RecipeView(ApiView):
from rest_framework_jwt.serializers import jwt_payload_handler

jwt_payload_handler
jwt.encode
settings