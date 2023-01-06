# Generated by Django 4.1.5 on 2023-01-06 17:20

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Beneficiary_entity",
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
                ("name", models.CharField(max_length=60)),
                ("data_do_cadastro", models.DateField()),
                ("update_do_cadastro", models.DateField()),
                ("email", models.EmailField(max_length=60)),
                ("cnpj", models.CharField(max_length=14)),
            ],
            options={
                "ordering": ("id",),
            },
        ),
    ]
