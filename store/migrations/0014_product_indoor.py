# Generated by Django 3.2 on 2021-06-05 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_saleprice_product_orgprice'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='indoor',
            field=models.BooleanField(default=False),
        ),
    ]
