from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("addresses", "0001_initial"),
        ("campaigns_projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="address",
            name="campaign_project",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaign_address",
                to="campaigns_projects.campaignsprojects",
            ),
        ),
    ]
