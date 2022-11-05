# Generated by Django 4.1.3 on 2022-11-05 14:08

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="ReportStates",
            fields=[
                (
                    "state_name",
                    models.CharField(max_length=63, primary_key=True, serialize=False),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportTypes",
            fields=[
                (
                    "type_name",
                    models.CharField(max_length=63, primary_key=True, serialize=False),
                ),
                ("lifespan", models.IntegerField(default=3600)),
            ],
        ),
        migrations.CreateModel(
            name="UsersData",
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
                ("firstname", models.CharField(default="", max_length=255)),
                ("surname", models.CharField(default="", max_length=255)),
                (
                    "age",
                    models.IntegerField(
                        validators=[django.core.validators.MinValueValidator(0)]
                    ),
                ),
                ("city", models.CharField(max_length=255)),
                (
                    "search_area",
                    models.IntegerField(
                        default=300,
                        validators=[
                            django.core.validators.MinValueValidator(100),
                            django.core.validators.MaxValueValidator(1000),
                        ],
                    ),
                ),
                ("points", models.IntegerField(default=0)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ReportTypesToAccept",
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
                (
                    "report_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.reporttypes",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Reports",
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
                ("latitude", models.FloatField()),
                ("altitude", models.FloatField()),
                ("time", models.DateTimeField(auto_now_add=True)),
                (
                    "max_people",
                    models.IntegerField(
                        default=None,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(1),
                            django.core.validators.MaxValueValidator(999),
                        ],
                    ),
                ),
                (
                    "current_people",
                    models.IntegerField(
                        default=0,
                        null=True,
                        validators=[
                            django.core.validators.MinValueValidator(0),
                            django.core.validators.MaxValueValidator(999),
                        ],
                    ),
                ),
                (
                    "description",
                    models.CharField(default=None, max_length=255, null=True),
                ),
                (
                    "report_state",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.reportstates",
                    ),
                ),
                (
                    "report_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="app.reporttypes",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "ordering": ["-time"],
            },
        ),
    ]
