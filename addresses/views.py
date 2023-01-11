from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import AddressSerializer
from .models import Address
from campaigns_projects.models import CampaignsProjects
import ipdb


class AddressView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = AddressSerializer
    queryset = Address.objects.all()

    
    def perform_create(self, serializer):
        campaign_id = self.kwargs["pk"]
        campaign = get_object_or_404(CampaignsProjects, pk=campaign_id)
        serializer.save(campaign_project=campaign)