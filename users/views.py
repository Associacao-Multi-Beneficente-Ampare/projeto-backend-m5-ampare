from rest_framework import generics
from rest_framework.views import APIView, Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from .pagination import CustomPageNumberPagination
from drf_spectacular.utils import extend_schema
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer
from .permissions import IsAdminOrReadOnly, IsAdminOrUser, IsOwner, IsVoluntary
from rest_framework.permissions import IsAdminUser
from .models import User
from campaigns_projects.models import CampaignsProjects
from rest_framework import status
import ipdb


class UserView(generics.CreateAPIView, CustomPageNumberPagination):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        tags=["users"],
        summary="create an user",
        description="create an user",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UserListInstitutionView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdminUser]

    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        tags=["users"],
        summary="List all users",
        description="List all users",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def get_queryset(self):
        route_parameter = self.request.GET.get("is_superuser")

        if route_parameter:

            queryset = User.objects.filter(is_superuser=True)
            return queryset

        return super().get_queryset()


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsOwner]


    serializer_class = UserSerializer
    queryset = User.objects.all()

    @extend_schema(
        tags=["users"],
        summary="list an user",
        description="list an user",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["users"],
        summary="edit an user",
        description="edit an user",
    )
    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    @extend_schema(
        tags=["users"],
        summary="delete an user",
        description="delete an user",
    )
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UserListVolunteersView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]

    permission_classes = [IsAdminUser]


    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get_queryset(self):
        route_parameter = self.request.GET.get("is_superuser")

        if route_parameter:

            queryset = User.objects.filter(is_superuser=False)
            return queryset

        return super().get_queryset()


class UserVoluntaryCampaignsProjectsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsVoluntary]

    def patch(self, request, pk):
        campaign = get_object_or_404(CampaignsProjects, pk=pk)
        campaign.voluntary_campaigns.add(request.user)
        if request.user.is_superuser:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(status=status.HTTP_204_NO_CONTENT)
