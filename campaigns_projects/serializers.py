from rest_framework import serializers
from .models import CampaignsProjects
from addresses.serializers import AddressSerializer
from addresses.models import Address


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

    """campaign_address = AddressSerializer()

     
    def create(self, validated_data: dict) -> CampaignsProjects:
        address_data = validated_data.pop("campaign_address")

        address,created = Address.objects.get_or_create(**address_data)
        campaign_obj = CampaignsProjects.objects.create(**validated_data, address=address)

        return campaign_obj"""