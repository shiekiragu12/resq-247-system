# Generated by Django 4.1.5 on 2023-02-22 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='tags',
            field=models.TextField(blank=True, null=True),
        ),
    ]