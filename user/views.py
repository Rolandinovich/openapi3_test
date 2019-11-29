import jwt
from django.conf import settings
from django.contrib.auth.hashers import make_password
from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import api_view, permission_classes
from rest_framework.mixins import UpdateModelMixin, RetrieveModelMixin
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny, IsAuthenticated
from user.serializers import UserInfoSerializer

from rest_framework.response import Response
from rest_framework_jwt.serializers import jwt_payload_handler

from user.models import User


# for rest_framework_jwt authtorizations, not use
# @api_view(['POST'])
# @permission_classes([AllowAny, ])
# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']
#
#         user = User.objects.get(email=email)
#         print(user.password, '=', make_password(password))
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['name'] = "%s %s" % (
#                     user.first_name, user.last_name)
#                 user_details['token'] = token
#                 # user_logged_in.send(sender=user.__class__,
#                 #                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)
#
#             except Exception as e:
#                 raise e
#         else:
#             res = {
#                 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
#             return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = {'error': 'please provide a email and a password'}
#         return Response(res)


class UserViewSet(RetrieveModelMixin, UpdateModelMixin, viewsets.GenericViewSet):
    permission_classes = (IsAuthenticated,)
    parser_classes = (MultiPartParser, FormParser,)
    serializer_class = UserInfoSerializer

    def get_object(self):
        return self.request.user
