# Generated by Django 4.0.4 on 2023-02-10 07:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacetical', '0002_remove_pharmacy_applicant_name_pharmacy_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pharmacy',
            name='user',
        ),
        migrations.AddField(
            model_name='pharmacy',
            name='applicant_name',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
