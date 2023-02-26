from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q

# Create your views here.


def dashboard(request):
    return render(request, template_name='doctor-dashboard/pages/index.html', context={})

def prescription(request):
    return render(request, template_name='doctor-dashboard/pages/pharmacy-index.html', context={})


def create_prescription(request):

    if request.method == 'POST':
        p_name = request.POST.get('p_name')
        p_code = request.POST.get('p_code')
        d_name = request.POST.get('d_name')
        d_name = request.POST.get('d_name')
        d_number = request.POST.get('d_number')
        dea = request.POST.get('dea')
        medication = request.POST.get('medication')
        dosage = request.POST.get('dosage')
        frequency = request.POST.get('frequency')
        subject = 'Form submission received'
        body = 'Hello your prescription has been made'
        email = EmailMessage(subject, body, to=[request.POST['p_code']])
        email.send()

        

        # user = User.objects.order_by('-pk')[0]

        prescription = PrescriptionPatient(first_name=first_name, last_name=last_name, pharma_name=pharma_name,
                            location=location, licence=licence, email=email, alternative_email=alternative_email, number=number, alternative_number=alternative_number, date_created=created_on, attach=attach)

        pharmacy.save()
        messages.success(
            request, 'Pharmacy created successfully wait for approval')
        return redirect('index')

    return render(request, template_name='pharmacy/verification-form.html', context={})
