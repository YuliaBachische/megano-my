# Generated by Django 5.0.3 on 2024-03-19 09:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0006_product"),
    ]

    operations = [
        migrations.CreateModel(
            name="ProductSeller",
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
                    "price",
                    models.DecimalField(decimal_places=2, default=0, max_digits=8),
                ),
                ("quantity", models.SmallIntegerField(default=0)),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="shopapp.product",
                    ),
                ),
                (
                    "seller",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="shopapp.seller"
                    ),
                ),
            ],
        ),
    ]
