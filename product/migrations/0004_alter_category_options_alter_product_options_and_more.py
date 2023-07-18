# Generated by Django 4.2.3 on 2023-07-15 00:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0003_category"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="category",
            options={"verbose_name": "Category", "verbose_name_plural": "Categories"},
        ),
        migrations.AlterModelOptions(
            name="product",
            options={"verbose_name": "Product", "verbose_name_plural": "Products"},
        ),
        migrations.AlterField(
            model_name="category",
            name="CATParent",
            field=models.ForeignKey(
                blank=True,
                limit_choices_to={"CATParent__isnull": True},
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="product.category",
                verbose_name="Main Parent",
            ),
        ),
        migrations.CreateModel(
            name="Product_Alternative",
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
                    "PALNAlternatives",
                    models.ManyToManyField(
                        related_name="alternative_products",
                        to="product.product",
                        verbose_name="Alternatives",
                    ),
                ),
                (
                    "PALNProduct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="main_prodcut",
                        to="product.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Alternative",
                "verbose_name_plural": "Product Alternatives",
            },
        ),
        migrations.CreateModel(
            name="Product_Accessories",
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
                    "PACCAlternatives",
                    models.ManyToManyField(
                        related_name="accessories_products",
                        to="product.product",
                        verbose_name="Accessories",
                    ),
                ),
                (
                    "PACCProduct",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="mainAccessory_prodcut",
                        to="product.product",
                        verbose_name="Product",
                    ),
                ),
            ],
            options={
                "verbose_name": "Product Accessory",
                "verbose_name_plural": "Product Accessories",
            },
        ),
    ]
