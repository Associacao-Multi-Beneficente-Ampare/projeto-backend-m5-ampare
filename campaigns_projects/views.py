from .models import CampaignsProjects
from .serializers import CampaignsProjectsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework import generics

class CampaignsProjectsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()

    def perform_create(self, serializer):
        userId = self.request.user 
        serializer.save(institution_campaigns=userId)
