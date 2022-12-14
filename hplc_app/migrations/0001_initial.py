# Generated by Django 4.1.2 on 2022-10-26 22:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ConvertImage",
            fields=[
                (
                    "filename",
                    models.CharField(
                        help_text="Enter csv filename",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="graph_input",
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
                ("x_min", models.IntegerField(null=True)),
                ("x_max", models.IntegerField(null=True)),
                ("y_min", models.IntegerField(null=True)),
                ("y_max", models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name="Image_Axes",
            fields=[
                (
                    "title",
                    models.CharField(
                        help_text="Enter an image title",
                        max_length=100,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("image", models.FileField(blank=True, null=True, upload_to="images/")),
                ("x_min", models.IntegerField(null=True)),
                ("x_max", models.IntegerField(null=True)),
                ("y_min", models.IntegerField(null=True)),
                ("y_max", models.IntegerField(null=True)),
            ],
        ),
    ]
