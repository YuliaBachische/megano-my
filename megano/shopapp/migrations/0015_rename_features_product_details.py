# Generated by Django 4.1 on 2024-04-09 19:18

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shopapp", "0014_product_features"),
    ]

    operations = [
        migrations.RenameField(
            model_name="product",
            old_name="features",
            new_name="details",
        ),
    ]
