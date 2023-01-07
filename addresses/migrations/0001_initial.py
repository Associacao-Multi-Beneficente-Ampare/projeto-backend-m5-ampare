from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Address",
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
                ("address", models.CharField(max_length=100, null=True)),
                ("number", models.CharField(max_length=50)),
                ("complement", models.CharField(max_length=120, null=True)),
                ("zipcode", models.CharField(max_length=50)),
                ("city_state", models.CharField(max_length=50, null=True)),
                ("neighborhood", models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
