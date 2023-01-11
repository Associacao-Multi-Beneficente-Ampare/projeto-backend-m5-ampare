from .models import CampaignsProjects
from .serializers import CampaignsProjectsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from rest_framework import generics
from .pagination import CustomPageNumberPagination
from drf_spectacular.utils import extend_schema


class CampaignsProjectsView(generics.ListCreateAPIView, CustomPageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()

    @extend_schema(
        tags=["CampaignsProjects"],
        summary="List a Campaigns Project",
        description="List a Campaigns Project",
    )
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @extend_schema(
        tags=["CampaignsProjects"],
        summary="Create a Campaigns Project",
        description="Create a Campaigns Project",
    )
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    """def perform_create(self, serializer):
        serializer.save(user=self.request.user)"""
