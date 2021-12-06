# Generated by Django 3.2 on 2021-06-05 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0014_product_indoor'),
    ]

    operations = [
        migrations.CreateModel(
            name='maintenance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=255)),
                ('slug', models.SlugField(max_length=255, unique=True)),
            ],
            options={
                'verbose_name_plural': 'maintenances',
            },
        ),
    ]