from django.shortcuts import render, redirect
from .models import *
from facilities.models import *
from django.db.models import Q
from sendfile import sendfile

# Create your views here.
def patient_dashboard(request):
    return render(request, template_name='patient-dashboard/pages/index.html', context={}) 

def medical(request):
    context={}
    context['patients'] = Patient.objects.all()
    return render(request, template_name='patient-dashboard/pages/medical-report.html', context=context)
def share_pdf(request):
    context={}
    context['patients'] = Patient.objects.all()
    pdf_url = request.GET.get('url')
    context = {'pdf_url': pdf_url}
    return render(request, template_name='patient-dashboard/pages/patient-list.html', context=context)

def view_pdf(request):
    
    file_path = 'media/prescription/prescription.pdf'
    return sendfile(request, file_path, attachment=True, attachment_filename='file.pdf')

def prescription(request):
    context={}
    context['patients'] = Patient.objects.all()
    return render(request, template_name='patient-dashboard/pages/patient-list.html', context=context) 

def progress(request):
    return render(request, template_name='patient-dashboard/pages/patient-details.html', context={}) 