# Generated by Django 4.2.3 on 2023-07-16 16:12

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("product", "0007_product_prdslug"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="PRDDiscountPrice",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=5, verbose_name="Discount Price"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="product",
            name="PRDISBestSeller",
            field=models.BooleanField(default=False, verbose_name="Best Seller"),
        ),
        migrations.AddField(
            model_name="product",
            name="PRDISNew",
            field=models.BooleanField(default=True, verbose_name="New Product "),
        ),
    ]
