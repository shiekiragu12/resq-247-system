# Generated by Django 4.1.5 on 2023-02-19 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacetical', '0011_rename_applicant_name_pharmacy_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='pharmacy',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
