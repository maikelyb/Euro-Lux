# Generated by Django 4.2.15 on 2024-09-07 08:46

from django.db import migrations, models
import packaging.models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Pack",
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
                (
                    "img",
                    models.ImageField(
                        null=True, upload_to=packaging.models.image_upload
                    ),
                ),
                ("title", models.CharField(max_length=50)),
                ("title_ar", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("description_ar", models.TextField()),
            ],
        ),
    ]
