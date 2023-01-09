from rest_framework import serializers
from .models import Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = [
            "id",
            "address",
            "number",
            "complement",
            "zipcode",
            "city_state",
            "neighborhood",
            "campaign_project_id",
        ]

        ##teste

    def create(self, validated_data):
        return Address.objects.create(**validated_data)
