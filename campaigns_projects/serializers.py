from rest_framework import serializers
from .models import CampaignsProjects
from addresses.serializers import AddressSerializer
from beneficiary_entity.serializers import BeneficiaryEntitySerializer

class CampaignsProjectsSerializer(serializers.ModelSerializer):
    campaign_address = AddressSerializer(read_only=True)
    beneficiary_entity = BeneficiaryEntitySerializer(read_only=True, many=True)

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
            "campaign_address",
            "beneficiary_entity",
        ]

        
    def create(self, validated_data: dict) -> CampaignsProjects:
        # address_data = validated_data.pop("campaign_address")
        # if address_data:
        #     address,created = Address.objects.get_or_create(**address_data)
        campaign_obj = CampaignsProjects.objects.create(**validated_data)

        return campaign_obj