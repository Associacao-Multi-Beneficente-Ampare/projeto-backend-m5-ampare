from .models import CampaignsProjects
from .serializers import CampaignsProjectsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework import generics
import ipdb


class CampaignsProjectsView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()


    def perform_create(self, serializer):
        userId = self.request.user
        serializer.save(institution_campaigns=userId)

class CampaignsProjectsDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    serializer_class = CampaignsProjectsSerializer
    queryset = CampaignsProjects.objects.all()

    lookup_url_kwarg = 'pk'
