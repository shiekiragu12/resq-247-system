from django.urls import path
from .views import *

app_name = 'doctor'

urlpatterns = [
    path('dashboard', dashboard, name="dashboard"),
    path('prescription', prescription, name="prescription"),
    # other URL patterns...
]
