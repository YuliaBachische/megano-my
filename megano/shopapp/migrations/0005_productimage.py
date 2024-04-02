# Generated by Django 5.0.3 on 2024-03-19 09:57

from django.db import migrations, models

import shopapp.models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0004_categories"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductImage",
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
                    "image",
                    models.ImageField(
                        upload_to=shopapp.models.product_images_directory_path
                    ),
                ),
                ("is_preview", models.BooleanField(default=False)),
            ],
        ),
    ]
