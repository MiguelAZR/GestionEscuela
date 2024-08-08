from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

from users.models import User
from users.api.serializers import UserSerializer

class UserApiViewSet(ModelViewSet):
    permission_class = [IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly]
    serializer_class = UserSerializer
    queryset = User.objects.all()