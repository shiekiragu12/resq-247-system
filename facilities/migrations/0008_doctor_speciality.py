# Generated by Django 4.1.5 on 2023-01-31 02:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0007_facility_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='speciality',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='facilities.facilityspeciality'),
        ),
    ]
