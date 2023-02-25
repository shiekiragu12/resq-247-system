from django.shortcuts import render, redirect
from .models import *
from django.db.models import Q
from django.contrib import messages
from django.core.mail import EmailMessage
from facilities.models import *
# Create your views here.


def create_pharmacy(request):

    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        pharma_name = request.POST.get('pharma_name')
        location = request.POST.get('location')
        licence = request.POST.get('licence')
        email = request.POST.get('email')
        alternative_email = request.POST.get('alternative_email')
        number = request.POST.get('number')
        alternative_number = request.POST.get('alternative_number')
        created_on = request.POST.get('created_on')
        attach= request.FILES.get('image')
        subject = 'Form submission received'
        body = 'Thank you for submitting the form your form is currently underreview'
        email = EmailMessage(subject, body, to=[request.POST['email']])
        email.send()
        
        existingpharmacy = Pharmacy.objects.filter(
            pharma_name=pharma_name).exists()

        # user = User.objects.order_by('-pk')[0]

        pharmacy = Pharmacy(first_name=first_name, last_name=last_name, pharma_name=pharma_name,
                            location=location, licence=licence, email=email, alternative_email=alternative_email, number=number, alternative_number=alternative_number, date_created=created_on, attach=attach)
        
        pharmacy.save()
        messages.success(request, 'Pharmacy created successfully wait for approval')
        return redirect('index')

    return render(request, template_name='pharmacy/verification-form.html', context={})

def send_order_email(request):
    # Get the user's email address from the request
    email = request.POST.get('email')
    
    # Send the email
    send_mail(
        'Order Confirmation',
        'Your order has been placed. Thank you!',
        'your-default-from-email',
        [email],
        fail_silently=False,
    )
    context={}
    context['patients'] = Patient.objects.all()
    # Render a template to display a confirmation message to the user
    return render(request, template_name='pharmacy-dashboard/pages/prescription-orders.html', context=context)


def pharmacy_dashboard(request):
    return render(request, template_name='pharmacy-dashboard/pages/index.html', context={})

def upload_product(request):
    return render(request, template_name='pharmacy-dashboard/pages/pharmacy-index.html', context={})

def live_product(request):
    context ={}
    context['live'] = Product.objects.filter(live_product=True)
    return render(request, template_name='pharmacy-dashboard/pages/live-product.html', context=context)

def pending_product(request):
    context ={}
    context['unapproved_products'] = Product.objects.filter(approved=False)
    return render(request, template_name='pharmacy-dashboard/pages/pending-product.html', context=context)

def pending_orders(request):
    context ={}
    context['unapproved_orders'] = Product.objects.filter(approved_order=False)
    return render(request, template_name='pharmacy-dashboard/pages/pending-orders.html', context=context)

def product_detail(request):
    return render(request, template_name='pharmacy-dashboard/pages/product-detail.html', context={})


def prescription_orders(request):
    context={}
    context['patients'] = Patient.objects.all()
    return render(request, template_name='pharmacy-dashboard/pages/prescription-orders.html', context=context)

def approved_product(request):
    context ={}
    context['approved_products'] = Product.objects.filter(approved=True)
    return render(request, template_name='pharmacy-dashboard/pages/approved-products.html', context=context)

def confirmed_orders(request):
    context ={}
    context['approved_orders'] = Product.objects.filter(delivered_order=True)
    return render(request, template_name='pharmacy-dashboard/pages/confirmed.html', context=context)

def unapproved_product(request):
    context ={}
    context['unapproved'] = Product.objects.filter(unapproved=True)
    return render(request, template_name='pharmacy-dashboard/pages/unapproved-products.html', context=context)

def pharmacy_report(request):
    return render(request, template_name='pharmacy-dashboard/pages/pharmacy-report.html', context={})

def create_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        brand = request.POST.get('brand')
        price = request.POST.get('price')
        discount = request.POST.get('discount')
        dom = request.POST.get('dom')
        description = request.POST.get('description')
        image = request.FILES.get('image') 
        code = request.POST.get('code')
          

        product = Product(name=name, discount=discount,brand=brand, price=price,  dom=dom, description=description, image=image,code=code)

        product.save()
        messages.success(request, 'Product uploaded successfully')
        return redirect('pharmacetical:upload-product')

    return render(request, template_name='pharmacy-dashboard/pages/pharmacy-index.html', context={})

