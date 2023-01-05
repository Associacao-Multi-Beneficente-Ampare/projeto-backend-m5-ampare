from django.db import models


class Address(models.Model):
    class Meta:
        ordering = ("id",)
        
    address = models.CharField(max_length=100, null=True)
    number = models.CharField(max_length=50)
    complement = models.CharField(max_length=120, null=True)
    zipcode = models.CharField(max_length=50)
    city_state = models.CharField(max_length=50, null=True)
    neighborhood = models.CharField(max_length=50, null=True)

    campaigns_projects = models.ForeignKey(
        "campaigns_projects.CampaignsProjects",
        on_delete=models.CASCADE,
        related_name="address"
    )





