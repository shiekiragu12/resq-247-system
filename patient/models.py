from django.db import models

# Create your models here.
class Prescription(models.Model):
    doctor_name = models.CharField(max_length=100, blank=True)
    patient_name = models.CharField(max_length=100, blank=True)
    patient_email = models.EmailField(max_length=254, blank=True, unique=True)
    postal_code= models.CharField(max_length=100, blank=True)
    address = models.CharField(max_length=100, blank=True)
    number = models.IntegerField(blank=True, null=True)
    gender = models.IntegerField(blank=True, null=True)
    city = models.TextField(blank=True)
    prescription = models.ImageField(upload_to='media/patient', blank=True, null=True)
    blood = models.IntegerField(blank=True, null=True)
    dob = models.DateField(blank=True, null=True)
    

    def __str__(self):
        return self.first_name+"'s "+self.doctor_name+" prescription"