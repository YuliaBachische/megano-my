# Generated by Django 5.0.3 on 2024-03-28 15:21

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0010_discount_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Review",
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
                ("description", models.TextField(blank=True)),
                ("created_reviews", models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
