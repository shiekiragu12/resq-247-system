# Generated by Django 4.1.5 on 2023-01-31 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0012_alter_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='facility',
            name='about_page_content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='home_page_content',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='facility',
            name='online_page_content',
            field=models.TextField(blank=True),
        ),
    ]