from django.urls import path
from .views import *

app_name = 'doctor'

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('prescription', prescription, name="prescription"),
    path('create-prescription', create_prescription, name="create-prescription"),
    path('view_prescription', view_prescription, name="view_prescription"),
    path('appointment', appointment, name="appointment"),
    path('create_appointment', create_appointment, name="create_appointment"), 
]
