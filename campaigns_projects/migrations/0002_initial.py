from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("campaigns_projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaignsprojects",
            name="voluntary_campaigns",
            field=models.ManyToManyField(
                related_name="campaigns_projects", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
