from django.db import models

# Create your models here.
class PrescriptionPatient(models.Model):
    p_name = models.CharField(max_length=100, blank=True)
    p_code = models.EmailField(max_length=100, blank=True)
    d_name = models.CharField(max_length=254, blank=True)
    d_number= models.CharField(max_length=100, blank=True)
    dea = models.CharField(max_length=100, blank=True)
    medication = models.CharField(blank=True, null=True, max_length=100,)
    dosage = models.CharField(blank=True, null=True,max_length=100)
    frequency = models.CharField(blank=True, max_length=100,)
    description = models.CharField(blank=True,max_length=100,)
    signature = models.IntegerField(blank=True, null=True)
    dop = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.p_name+"'s "+self.p_name+" prescriptionpatient"                                                                                   

class Appointment(models.Model):
    patient = models.CharField(max_length=100, blank=True)
    p_email = models.EmailField(max_length=100, blank=True)
    date = models.DateField(max_length=100, blank=True)
    start_time = models.TimeField(max_length=254, blank=True)
    end_time= models.TimeField(max_length=100, blank=True)
    doctor = models.CharField(max_length=100, blank=True)
    injury = models.CharField(blank=True, null=True, max_length=100,)
    note = models.CharField(blank=True, null=True,max_length=100)
    

    def __str__(self):
        return self.patient+"'s "+self.patient+" appointment"  