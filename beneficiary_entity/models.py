from django.db import models
import uuid


class BeneficiaryEntity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    date_created = models.DateField(auto_now_add=False)
    date_updated = models.DateField(auto_now=False)
    email = models.EmailField(max_length=60)
    cnpj = models.CharField(max_length=14, unique=True)

    campaigns_projects = models.ManyToManyField(
        "campaigns_projects.CampaignsProjects",
        related_name="beneficiary_entity",
    )