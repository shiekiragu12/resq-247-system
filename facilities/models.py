from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


# Create your models here.


class County(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Constituency(models.Model):
    name = models.CharField(max_length=400, blank=False, null=False)
    county = models.ForeignKey(County, blank=True, null=True, on_delete=models.SET_NULL)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Condition(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    factsheet = models.TextField(blank=True, null=True)
    pathogen = models.TextField(blank=True, null=True)
    clinical_features = models.TextField(blank=True, null=True)
    transmission = models.TextField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    treatment = models.TextField(blank=True, null=True)
    prevention = models.TextField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FacilitySpeciality(models.Model):
    name = models.CharField(max_length=100)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class FacilityType(models.Model):
    name = models.TextField(blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(FacilityType, self).save(*args, **kwargs)


class Facility(models.Model):
    CHOICES = (
        ('pharmacy', 'Pharmacy'),
        ('clinic', 'Clinic'),
        ('nutraceuticals', 'Nutraceuticals')
    )
    owner = models.ForeignKey(User, blank=True, null=True, on_delete=models.SET_NULL)
    owner_name = models.TextField(blank=True, null=True)

    facility_type = models.ForeignKey(FacilityType, blank=True, null=True, on_delete=models.SET_NULL)
    facility_kind = models.CharField(max_length=100, blank=True, null=True, choices=CHOICES)    # pharmacy, clinic,
    # nutraceuticals

    name = models.CharField(max_length=200, blank=False, null=False)
    slug = models.SlugField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    location = models.CharField(max_length=100, blank=True, null=False, default="")
    city = models.CharField(max_length=100, blank=True, null=False, default="")

    county = models.ForeignKey(County, on_delete=models.SET_NULL, null=True, blank=False)
    constituency = models.ForeignKey(Constituency, on_delete=models.SET_NULL, null=True, blank=False)

    latitude = models.CharField(max_length=100, blank=False, null=False, default="")
    longitude = models.CharField(max_length=100, blank=False, null=False, default="")

    status = models.BooleanField(default=False)

    email = models.CharField(max_length=100, blank=True, null=False, default="")
    contact_no = models.CharField(max_length=100, blank=True, null=False, default="")
    address = models.CharField(max_length=300, blank=True, null=False, default="")

    shared_encounters = models.ManyToManyField('Encounter', blank=True, related_name='shared_encounters')

    specialities = models.ManyToManyField(FacilitySpeciality, blank=True)

    authorized = models.BooleanField(default=False)

    logo = models.FileField(upload_to='facilities/files/logo/', null=True, blank=True)
    cover_image = models.FileField(upload_to='facilities/files/covers/', null=True, blank=True)

    home_page_content = models.TextField(blank=True)
    about_page_content = models.TextField(blank=True)
    online_page_content = models.TextField(blank=True)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Facility, self).save(*args, **kwargs)


class Doctor(models.Model):
    facilities = models.ManyToManyField(Facility, blank=True)
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    description = models.TextField()
    specialities = models.ManyToManyField(FacilitySpeciality, blank=True)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Qualification(models.Model):
    doctor = models.ForeignKey(Doctor, blank=True, null=False, on_delete=models.CASCADE, related_name='qualifications')
    degree = models.CharField(max_length=10, blank=False, null=False)
    university = models.CharField(max_length=10, blank=False, null=False)
    year = models.CharField(max_length=10, blank=False, null=False)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Staff(models.Model):
    facility = models.ForeignKey(Facility, blank=True, null=True, on_delete=models.SET_NULL)
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)
    designation = models.TextField()
    education = models.TextField()

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Patient(models.Model):
    facility = models.ForeignKey(Facility, blank=True, null=True, on_delete=models.SET_NULL, related_name='patients')
    facilities = models.ManyToManyField(Facility, blank=True, related_name='facilities')
    user = models.OneToOneField(User, blank=False, null=False, on_delete=models.CASCADE)
    blood_group = models.CharField(max_length=5)
    dob = models.DateField()
    account_sharable = models.BooleanField(default=False)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"


class Service(models.Model):
    facility = models.ForeignKey(Facility, blank=True, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, blank=True, null=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()
    category = models.ForeignKey('ServiceCategory', blank=False, null=False, on_delete=models.CASCADE)
    charges = models.FloatField()
    duration = models.IntegerField()
    status = models.BooleanField(default=True)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ServiceCategory(models.Model):
    name = models.CharField(max_length=200, blank=False, null=False)
    description = models.TextField()

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    facility = models.ForeignKey(Facility, blank=True, null=True, on_delete=models.SET_NULL,
                                 related_name="facility_appointments")
    doctor = models.ForeignKey(Doctor, blank=False, null=True, on_delete=models.SET_NULL,
                               related_name="doctor_appointments")
    patient = models.ForeignKey(Patient, blank=False, null=True, on_delete=models.SET_NULL,
                                related_name="patient_appointments")
    note = models.TextField()
    status = models.BooleanField(default=False)
    date = models.DateTimeField()
    start_time = models.CharField(max_length=10, blank=False, null=False, default="")
    end_time = models.CharField(max_length=10, blank=False, null=False, default="")
    condition = models.ForeignKey(Condition, blank=False, null=True, on_delete=models.CASCADE)

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.user.username


class MedicalFile(models.Model):
    appointment = models.ForeignKey(Appointment, blank=False, null=True, on_delete=models.SET_NULL,
                                    related_name='appointment_medical_files')
    encounter = models.ForeignKey('Encounter', blank=True, null=True, on_delete=models.CASCADE,
                                  related_name='encounter_medical_files')
    file = models.FileField(upload_to='facilities/files/medical/')

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)


class Encounter(models.Model):
    facility = models.ForeignKey(Facility, blank=True, null=True, on_delete=models.SET_NULL)
    doctor = models.ForeignKey(Doctor, blank=False, null=True, on_delete=models.SET_NULL,
                               related_name="doctor_encounters")
    patient = models.ForeignKey(Patient, blank=False, null=True, on_delete=models.SET_NULL,
                                related_name="patient_encounters")
    description = models.TextField()
    date = models.DateTimeField()

    created_on = models.DateTimeField(auto_now=True, auto_created=True)
    updated_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.user.username
