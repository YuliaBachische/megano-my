# Generated by Django 5.0.3 on 2024-05-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0036_merge_20240525_1315"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(default=123, verbose_name="номер телефона"),
            preserve_default=False,
        ),
    ]
