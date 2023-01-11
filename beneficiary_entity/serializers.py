from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import BeneficiaryEntity
from campaigns_projects.models import CampaignsProjects
import ipdb

class BeneficiaryEntitySerializer(serializers.ModelSerializer):
    class Meta:
        model = BeneficiaryEntity
        fields = [
            "id",
            "name",
            "date_created",
            "date_updated",
            "email",
            "cnpj",
        ]

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=BeneficiaryEntity.objects.all())],
    )


    def create(self, validated_data: dict) -> BeneficiaryEntity:
        campaigns_data = validated_data.pop("campaigns_projects")

        entity = BeneficiaryEntity.objects.create(**validated_data)

        entity.campaigns_projects.add(campaigns_data)
        
        return entity


    def update(self, instance: BeneficiaryEntity, validated_data: dict) -> BeneficiaryEntity:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance