# Generated by Django 4.1.5 on 2023-01-11 21:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("campaigns_projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="campaignsprojects",
            name="user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="campaigns",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="campaignsprojects",
            name="voluntary_campaigns",
            field=models.ManyToManyField(
                related_name="campaigns_projects", to=settings.AUTH_USER_MODEL
            ),
        ),
    ]
