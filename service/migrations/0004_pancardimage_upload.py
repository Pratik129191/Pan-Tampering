# Generated by Django 4.2.7 on 2023-11-19 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("service", "0003_panoriginal"),
    ]

    operations = [
        migrations.AddField(
            model_name="pancardimage",
            name="upload",
            field=models.ImageField(blank=True, null=True, upload_to="service/images"),
        ),
    ]
