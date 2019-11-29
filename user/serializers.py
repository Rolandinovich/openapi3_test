from rest_framework import serializers

from user.models import User


class UserInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'avatar', 'email')
        read_only_fields = ('id', 'email')
