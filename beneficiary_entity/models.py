from django.db import models
from beneficiary_entity import CampaignsProjects
import uuid

class Beneficiary_entity(models.Model):
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=60)
    data_do_cadastro = models.DateField(auto_now_add=False)
    update_do_cadastro = models.DateField(auto_now=False)
    email = models.EmailField(max_length=60)
    cnpj = models.CharField(max_length=14)

    campaigns_projects = models.ManyToManyField(CampaignsProjects)
