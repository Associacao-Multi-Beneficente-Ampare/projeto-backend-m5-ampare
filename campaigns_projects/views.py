from .models import CampaignsProjects
from .serializers import CampaignsProjectsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
from .pagination import CustomPageNumberPagination
from drf_spectacular.utils import extend_schema
import ipdb




class CampaignsProjectsView(generics.ListCreateAPIView, CustomPageNumberPagination):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()


    @extend_schema(
        tags=["CampaignsProjects"],
        summary="List a Campaigns Project",
        description="List a Campaigns Project",
    )
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    @extend_schema(
        tags=["CampaignsProjects"],
        summary="Create a Campaigns Project",
        description="Create a Campaigns Project",
    )
    def post(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


    def perform_create(self, serializer):
        userId = self.request.user
        serializer.save(institution_campaigns=userId)

class CampaignsProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()

    lookup_url_kwarg = 'pk'

