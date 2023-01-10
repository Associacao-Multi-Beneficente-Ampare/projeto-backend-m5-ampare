from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BeneficiaryEntity",
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
                ("date_created", models.DateField()),
                ("date_updated", models.DateField()),
                ("email", models.EmailField(max_length=60)),
                ("cnpj", models.CharField(max_length=14, unique=True)),
            ],
        ),
    ]
