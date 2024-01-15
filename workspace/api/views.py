from rest_framework import viewsets

from .serializer import UserModelSerializer
from workspace.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserModelSerializer