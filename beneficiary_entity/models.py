from django.db import models
from beneficiary_entity import CampaignsProjects


class Beneficiary_entity(models.Model):
    class Meta:
        ordering = ("id",)

    name = models.CharField(max_length=60)
    data_do_cadastro = models.DateField(auto_now_add=False)
    update_do_cadastro = models.DateField(auto_now=False)
    email = models.EmailField(max_length=60)
    cnpj = models.CharField(max_length=14)

    campaigns_projects = models.ManyToManyField(CampaignsProjects)
