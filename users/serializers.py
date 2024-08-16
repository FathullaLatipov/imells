from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password

from django.contrib.auth.models import User as MyUser


class UserDataSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=False,
                                     validators=[validate_password])

    class Meta:
        model = MyUser
        fields = '__all__'
