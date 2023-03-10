# Generated by Django 4.1.5 on 2023-02-22 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('facilities', '0027_alter_appointment_doctor_alter_appointment_facility_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='encounter',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_encounters', to='facilities.doctor'),
        ),
        migrations.AlterField(
            model_name='encounter',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_encounters', to='facilities.patient'),
        ),
    ]
