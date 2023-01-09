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
            "campaign_address"
        ]
        read_only_fields = ["campaign_address"]

    campaign_address = AddressSerializer()

     
    def create(self, validated_data: dict) -> CampaignsProjects:
        # address_data = validated_data.pop("campaign_address")
        # if address_data:
        #     address,created = Address.objects.get_or_create(**address_data)
        campaign_obj = CampaignsProjects.objects.create(**validated_data)

        return campaign_obj