from django.db import models
import uuid


class Address(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    address = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=50)
    complement = models.CharField(max_length=120, null=True)
    zipcode = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50, null=True)
    neighborhood = models.CharField(max_length=50, null=True)

    campaign_project = models.OneToOneField(
        "campaigns_projects.CampaignsProjects",
        on_delete=models.CASCADE,
        related_name="campaign_address",
    )
