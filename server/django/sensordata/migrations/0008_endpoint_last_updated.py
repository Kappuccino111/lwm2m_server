# Generated by Django 5.0.1 on 2024-01-29 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("sensordata", "0007_alter_endpoint_endpoint"),
    ]

    operations = [
        migrations.AddField(
            model_name="endpoint",
            name="last_updated",
            field=models.DateTimeField(auto_now=True),
        ),
    ]