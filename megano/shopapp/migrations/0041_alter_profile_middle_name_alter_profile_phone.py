# Generated by Django 5.0.3 on 2024-05-26 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shopapp", "0040_alter_profile_seller"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="middle_name",
            field=models.CharField(max_length=255, null=True, verbose_name="отчество"),
        ),
        migrations.AlterField(
            model_name="profile",
            name="phone",
            field=models.IntegerField(null=True, verbose_name="номер телефона"),
        ),
    ]
