# Generated by Django 4.1.5 on 2023-01-06 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("campaigns_projects", "__first__"),
    ]

    operations = [
        migrations.CreateModel(
            name="Address",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("address", models.CharField(max_length=100, null=True)),
                ("number", models.CharField(max_length=50)),
                ("complement", models.CharField(max_length=120, null=True)),
                ("zipcode", models.CharField(max_length=50)),
                ("city_state", models.CharField(max_length=50, null=True)),
                ("neighborhood", models.CharField(max_length=50, null=True)),
                (
                    "campaigns_projects",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="address",
                        to="campaigns_projects.campaignsprojects",
                    ),
                ),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]
