from django.db import models

# Create your models here.
class PrescriptionPatient(models.Model):
    p_name = models.CharField(max_length=100, blank=True)
    p_email = models.EmailField(max_length=100, blank=True, unique=True)
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