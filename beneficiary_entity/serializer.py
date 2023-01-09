from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import BeneficiaryEntity


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
        return BeneficiaryEntity.objects.create(**validated_data)

    def update(
        self, instance: BeneficiaryEntity, validated_data: dict
    ) -> BeneficiaryEntity:
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
