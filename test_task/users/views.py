from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet


from .models import User
from .serializers import UserSerializer, UserDetailSerializer


class UserView(mixins.CreateModelMixin,
               mixins.RetrieveModelMixin,
               mixins.UpdateModelMixin,
               mixins.DestroyModelMixin,
               GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class UserListView(mixins.ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

