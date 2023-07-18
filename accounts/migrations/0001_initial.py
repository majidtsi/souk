# Generated by Django 4.2.3 on 2023-07-17 13:21

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Profile",
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
                ("slug", models.SlugField(blank=True, null=True)),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="profile_img",
                        verbose_name="image",
                    ),
                ),
                ("country", models.CharField(max_length=100, verbose_name="Country")),
                ("adress", models.CharField(max_length=100)),
                (
                    "join_date",
                    models.DateTimeField(
                        default=datetime.datetime.now, verbose_name="join date"
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "Profile",
                "verbose_name_plural": "Profiles",
            },
        ),
    ]
