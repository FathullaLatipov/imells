from django.urls import path, include
from rest_framework.routers import DefaultRouter
from users.views import UserListAPIView

router = DefaultRouter()
router.register(r'users', UserListAPIView, basename='videos')


urlpatterns = [

]

urlpatterns += [
    path('v1/', include(router.urls)),
]