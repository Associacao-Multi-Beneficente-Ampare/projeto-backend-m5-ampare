from rest_framework import serializers
from .models import CampaignsProjects


class CampaignsProjectsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CampaignsProjects
        fields = [
            "id",
            "name",
            "is_active",
            "start",
            "end",
            "date_created",
            "date_update",
            "age_majority",
        ]

    def create(self, validated_data):
        return CampaignsProjects.objects.create(**validated_data)