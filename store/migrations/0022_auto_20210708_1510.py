# Generated by Django 3.2 on 2021-07-08 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0021_alter_product_nickname'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='big',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.IntegerField(),
        ),
    ]
