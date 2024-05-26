# Generated by Django 5.0.3 on 2024-05-26 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("pay", "0014_remove_order_payment_type_alter_order_delivery_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="payment",
            field=models.CharField(
                choices=[("cash", "Cash"), ("credit_card", "Credit card")],
                default="cash",
                max_length=100,
                verbose_name="оплата",
            ),
        ),
    ]
