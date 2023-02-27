from django.shortcuts import render, redirect
from .models import *
from facilities.models import *
from doctor.models import *
from django.db.models import Q

# Create your views here.


def patient_dashboard(request):
    return render(request, template_name='patient-dashboard/pages/index.html', context={})


def medical(request):
    context = {}
    context['patients'] = Patient.objects.all()
    return render(request, template_name='patient-dashboard/pages/medical-report.html', context=context)


def share_pdf(request):
    context = {}
    context['patients'] = Patient.objects.all()
    try:
        context['prescription'] = PrescriptionPatient.objects.get(p_code =request.user.email)
    except Prescription.DoesNotExist:
        prescription = None
    
    pdf_url = request.GET.get('url')
    context = {'pdf_url': pdf_url}
    return render(request, template_name='patient-dashboard/pages/patient-list.html', context=context)


def prescription(request):
    context = {}
    context['patients'] = Patient.objects.all()
    return render(request, template_name='patient-dashboard/pages/patient-list.html', context=context)


def progress(request):
    return render(request, template_name='patient-dashboard/pages/patient-details.html', context={})
