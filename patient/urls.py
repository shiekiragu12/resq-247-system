from django.urls import path
from .views import *

app_name = 'patient'

urlpatterns = [
    path('dashboard', patient_dashboard, name='dashboard'),
    path('prescription', prescription, name='prescription'),
    path('progress', progress, name='progress'),
    path('medical-report', medical, name='medical-report'),
    path('pdf', view_pdf, name='view_pdf'),
    # other URL patterns...
]
