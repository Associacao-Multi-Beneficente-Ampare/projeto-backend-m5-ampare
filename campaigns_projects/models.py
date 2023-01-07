from django.db import models
import uuid

class CampaignsProjects(models.Model):
    
    id = models.UUIDField(default=uuid.uuid4, primary_key=True, editable=False)
    name = models.CharField(max_length=100)
    is_active= models.BooleanField(default=True, null=True)
    start = models.DateField()
    end = models.DateField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_update = models.DateField(auto_now=True)
    age_majority = models.BooleanField(default=True, null=True)


    institution_campaigns = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="project",
    )

    voluntary_campaigns = models.ManyToManyField(
        "users.User",
        related_name="campaign",
    )
    
    def __repr__(self) -> str:
        return f"<CampaignsProjects [{self.id}] - {self.name}>"

