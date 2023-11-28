from django.contrib.auth.models import User
from rest_framework import permissions
from auth.serializers.user import UserSerializer
from rest_framework.generics import ListCreateAPIView
from rest_framework import viewsets


# class UserListCreateView(viewsets.ModelViewSet):
#     """
#     A viewset for viewing and editing user instances.
#     """
#     serializer_class = UserSerializer
#     queryset = User.objects.all()


class UserListCreateView(ListCreateAPIView):    
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]