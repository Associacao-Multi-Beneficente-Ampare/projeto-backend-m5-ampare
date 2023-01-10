# Generated by Django 4.1.5 on 2023-01-09 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("beneficiary_entity", "0001_initial"),
        ("campaigns_projects", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="beneficiaryentity",
            name="campaigns_projects",
            field=models.ManyToManyField(
                related_name="beneficiary_entity",
                to="campaigns_projects.campaignsprojects",
            ),
        ),
    ]
