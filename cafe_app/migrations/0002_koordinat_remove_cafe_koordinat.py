# Generated by Django 4.1.2 on 2023-01-02 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("cafe_app", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Koordinat",
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
                ("nama_cafe", models.CharField(max_length=50)),
                ("koordinat", models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(model_name="cafe", name="koordinat",),
    ]
