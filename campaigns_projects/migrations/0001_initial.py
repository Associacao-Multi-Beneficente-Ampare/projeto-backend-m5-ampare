from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="CampaignsProjects",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=True, null=True)),
                ("start", models.DateField()),
                ("end", models.DateField()),
                ("date_created", models.DateTimeField(auto_now_add=True)),
                ("date_update", models.DateField(auto_now=True)),
                ("age_majority", models.BooleanField(default=True, null=True)),
            ],
        ),
    ]
