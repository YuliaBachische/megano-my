# Generated by Django 5.0.3 on 2024-04-24 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0015_alter_productseller_product"),
    ]

    operations = [
        migrations.AddField(
            model_name="categories",
            name="archived",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="categories",
            name="name",
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
