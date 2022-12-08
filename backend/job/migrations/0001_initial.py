# Generated by Django 4.1.4 on 2022-12-07 20:30

from django.conf import settings
import django.contrib.gis.db.models.fields
import django.contrib.gis.geos.point
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Job",
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
                ("title", models.CharField(max_length=200, null=True)),
                ("description", models.TextField(null=True)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("address", models.CharField(max_length=100, null=True)),
                (
                    "jobType",
                    models.CharField(
                        choices=[
                            ("Permanent", "Permanent"),
                            ("Internship", "Internship"),
                            ("Temporary", "Temporary"),
                        ],
                        default="Permanent",
                        max_length=10,
                    ),
                ),
                (
                    "education",
                    models.CharField(
                        choices=[
                            ("Bachelors", "Bachelors"),
                            ("Masters", "Masters"),
                            ("Phd", "Phd"),
                        ],
                        default="Bachelors",
                        max_length=10,
                    ),
                ),
                (
                    "industry",
                    models.CharField(
                        choices=[
                            ("IT", "It"),
                            ("Business", "Business"),
                            ("Banking", "Banking"),
                            ("Education", "Education"),
                            ("Telecommunication", "Telecommunication"),
                            ("Others", "Others"),
                        ],
                        default="Business",
                        max_length=30,
                    ),
                ),
                (
                    "experience",
                    models.CharField(
                        choices=[
                            ("No Experience", "No Experience"),
                            ("1 years", "One Year"),
                            ("2 years", "Two Years"),
                            ("3 years plus", "Three Years Above"),
                        ],
                        default="No Experience",
                        max_length=20,
                    ),
                ),
                (
                    "salary",
                    models.IntegerField(
                        default=1,
                        validators=[
                            django.core.validators.MinLengthValidator(1),
                            django.core.validators.MaxLengthValidator(99999999999),
                        ],
                    ),
                ),
                ("position", models.IntegerField(default=1)),
                ("company", models.CharField(max_length=100, null=True)),
                (
                    "point",
                    django.contrib.gis.db.models.fields.PointField(
                        default=django.contrib.gis.geos.point.Point(0.0, 0.0), srid=4326
                    ),
                ),
                ("lastDate", models.DateTimeField(default=job.models.ReturnDateTime)),
                ("createdAt", models.DateTimeField(auto_now_add=True)),
                ("updatedAt", models.DateTimeField(auto_now=True)),
                (
                    "user",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]
