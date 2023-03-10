# Generated by Django 4.1.5 on 2023-02-21 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0020_facility_facility_kind_alter_medicalfile_appointment_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constituency',
            name='county',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='constituencies', to='facilities.county'),
        ),
    ]
