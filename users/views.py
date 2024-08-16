from django.shortcuts import render

from rest_framework.viewsets import GenericViewSet, mixins

from users.serializers import UserDataSerializer
from django.contrib.auth.models import User as MyUser


class UserListAPIView(mixins.RetrieveModelMixin,
                      mixins.CreateModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin,
                      GenericViewSet):
    queryset = MyUser.objects.all()
    serializer_class = UserDataSerializer
