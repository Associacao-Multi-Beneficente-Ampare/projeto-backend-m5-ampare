from rest_framework import serializers
from .models import Beneficiary_entity


class BeneficiaryEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Beneficiary_entity
        fields = [
            "id",
            "name",
            "data_do_cadastro",
            "update_do_cadastro",
            "email",
            "cnpj",
        ]

    def create(self, validated_data):
        return Beneficiary_entity.objects.create(**validated_data)
