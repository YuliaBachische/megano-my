# Generated by Django 5.0.3 on 2024-05-20 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pay", "0009_alter_order_address_alter_order_city_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.CharField(
                choices=[("someone", "Someone"), ("online", "Online")],
                default="someone",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="transaction",
            name="payment_status",
            field=models.CharField(
                choices=[
                    ("paid", "Paid"),
                    ("running", "Running"),
                    ("cancelled", "Cancelled"),
                ],
                default="running",
                max_length=100,
            ),
        ),
    ]
