# Generated by Django 4.1.5 on 2023-02-24 02:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacetical', '0015_pharmacy_attach_product_code_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='approved_order',
            field=models.BooleanField(default=False),
        ),
    ]
