from django.shortcuts import render, redirect
from .models import *
import re
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage
from django.core.files.base import ContentFile
from django.template.loader import render_to_string
from django.core.files.storage import FileSystemStorage
from django.http import FileResponse
from django.template.loader import get_template
from io import BytesIO
from reportlab.pdfgen import canvas

# Create your views here.
def dashboard(request):
    return render(request, template_name='doctor-dashboard/pages/index.html', context={})

def prescription(request):
    return render(request, template_name='doctor-dashboard/pages/pharmacy-index.html', context={})

def appointment(request):
    context={}
    context['appointment']=Appointment.objects.all()
    return render(request, template_name='doctor-dashboard/pages/appointment.html', context=context)

def view_prescription(request):
    context={}
    context['prescription']=PrescriptionPatient.objects.all()
    return render(request, template_name='doctor-dashboard/pages/view-prescription.html', context=context)

def create_appointment(request):

    if request.method == 'POST':
        patient = request.POST.get('patient')
        p_email = request.POST.get('p_email')
        date = request.POST.get('date')
        start_time = request.POST.get('start_time')
        end_time = request.POST.get('end_time')
        doctor = request.POST.get('doctor')
        injury = request.POST.get('injury')
        note = request.POST.get('note')

        # Send the email with the prescription PDF attached
        subject = 'Doctor appointment with '+ doctor
        body = 'Hello,'+ patient +' your appointment is on ' + date + ' kindly avail yourself'
        email = EmailMessage(subject, body, to=[p_email])
        email.send()       

        # user = User.objects.order_by('-pk')[0]

        appointment = Appointment(patient=patient, p_email =p_email, date=date,
                            start_time=start_time, end_time=end_time, doctor=doctor, injury=injury, note=note)

        appointment.save()

    
        messages.success(
            request, 'Appointment has been sent to patient successfully')
        return redirect('doctor:appointment')

    return render(request, template_name='doctor-dashboard/pages/appointment.html', context={})

def create_prescription(request):

    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_code = request.POST.get('p_code')
        d_name = request.POST.get('d_name')
        d_number = request.POST.get('d_number')
        dea = request.POST.get('dea')
        medication = request.POST.get('medication')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        description = request.POST.get('description')
        
         # Generate the prescription PDF using a template and context data
        context = {
            'p_name': p_name,
            'p_code': p_code,
            'd_name': d_name,
            'd_number': d_number,
            'dea': dea,
            'medication': medication,
            'dosage': dosage,
            'frequency': frequency,
            'description': description,
        }
       
        prescription_html = render_to_string('doctor-dashboard/pages/prescription.html', context)

        # Save the prescription PDF to the media folder
        fs = FileSystemStorage(location=settings.MEDIA_ROOT + '/prescription/')
        filename = f'prescription_{p_code.replace("@", "-")}.pdf'
        file = fs.save(filename, ContentFile(prescription_html.encode('utf-8')))
        prescription_pdf = fs.path(file)

        # Send the email with the prescription PDF attached
        subject = 'Prescription for ' + p_name
        body = 'Hello, please find your prescription attached.'
        email = EmailMessage(subject, body, to=[p_code])

        # Attach the prescription PDF file to the email
        with open(prescription_pdf, 'rb') as f:
            email.attach(filename, f.read(), 'application/pdf')

        email.send()       

        # user = User.objects.order_by('-pk')[0]

        prescription = PrescriptionPatient(p_name=p_name, p_code =p_code, d_name=d_name,
                            d_number=d_number, dea=dea, medication=medication, dosage=dosage, frequency=frequency,description=description)

        prescription.save()

    
        messages.success(
            request, 'Prescription sent to patient successfully')
        return redirect('doctor:dashboard')

    return render(request, template_name='doctor-dashboard/pages/index.html', context={})
