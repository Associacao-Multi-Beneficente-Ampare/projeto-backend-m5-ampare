from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "name",
            "username",
            "password",
            "cnpj",
            "birth",
            "telephone",
            "email",
            "is_superuser",
            "is_institution",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser":{"write_only": True},
        }
    is_institution = serializers.BooleanField(source='is_superuser')

    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    
    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(**validated_data)

    def update(self, instance: User, validated_data: dict) -> User:
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance
