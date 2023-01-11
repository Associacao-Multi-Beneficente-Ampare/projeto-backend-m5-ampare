from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from users.permissions import IsAdminOrReadOnly
from django.shortcuts import get_object_or_404
from .serializers import BeneficiaryEntitySerializer
from .models import BeneficiaryEntity
from campaigns_projects.models import CampaignsProjects
from campaigns_projects.serializers import CampaignsProjectsSerializer
import ipdb


class BeneficiaryEntityView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAdminOrReadOnly]
    serializer_class = BeneficiaryEntitySerializer
    queryset = BeneficiaryEntity.objects.all()


    def perform_create(self, serializer):
        campaign_id = self.kwargs["pk"]
        campaign = get_object_or_404(CampaignsProjects, pk=campaign_id)
        serializer.save(campaigns_projects=campaign)
