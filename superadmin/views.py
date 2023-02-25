from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from mailer.models import Email, EmailConfiguration
from facilities.models import Doctor, Patient, Staff, County, Constituency, Service, ServiceCategory, Condition, \
    FacilitySpeciality, Facility, FacilityType, Appointment, Encounter
from shop.models import Category, Product, Order
from mainapp.models import Blog, Tag
from .decorators import admin_only
# Create your views here.


@admin_only
def dashboard(request):
    users_ = User.objects.all()
    doctors_ = Doctor.objects.all()
    staff_ = Staff.objects.all()
    patients_ = Patient.objects.all()
    facilities_ = Facility.objects.all()
    facility_types_ = FacilityType.objects.all()
    products_ = Product.objects.all()
    specialities_ = FacilitySpeciality.objects.all()
    diseases_ = Condition.objects.all()
    blogs_ = Blog.objects.all()

    context = {
        "users_count": users_.count(),
        "users": users_.order_by('-id')[0:5],
        "doctors_count": doctors_.count(),
        "staff_count": staff_.count(),
        "patients_count": patients_.count(),
        "facilities": facilities_.order_by('-id')[0:5],
        "clinics_count": facilities_.filter(facility_kind="clinic").count(),
        "pharmacies_count": facilities_.filter(facility_kind='pharmacy').count(),
        "nutraceutacals_count": facilities_.filter(facility_kind='nutraceuticals').count(),
        "facility_types_count": facility_types_.count(),
        "products": products_.order_by('id')[0:5],
        "live_products_count": products_.filter(approved=True).count(),
        "pending_products_count": products_.filter(approved=False).count(),
        "specialities_count": specialities_.count(),
        "diseases_count": diseases_.count(),
        "blogs": blogs_.order_by('-id')[0:5],
        "total_blogs": blogs_.count()
    }
    return render(request, template_name='super-admin-dashboard/pages/index.html', context=context)


# Users
@admin_only
def users(request):
    users_ = User.objects.all()
    context = {
        "users": users_,
        "total_users": users_.count(),
        "total_admins": users_.filter(is_superuser=True).count(),
        "active_users": users_.filter(is_active=True).count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/users/users.html', context=context)


@admin_only
def doctors(request):
    doctors_ = Doctor.objects.all()
    context = {
        "doctors": doctors_,
        "total_doctors": doctors_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/users/doctors.html', context=context)


@admin_only
def staff(request):
    staff_ = Staff.objects.all()
    context = {
        "staff": staff_,
        "total_staff": staff_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/users/staff.html', context=context)


@admin_only
def patients(request):
    patients_ = Patient.objects.all()
    context = {
        "patients": patients_,
        "total_patients": patients_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/users/patients.html', context=context)


# Emails
@admin_only
def emails(request):
    emails_ = Email.objects.all()
    context = {
        "emails": emails_,
        "total_emails": emails_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/emails/emails.html', context=context)


@admin_only
def emailconfigs(request):
    emailconfigs_ = EmailConfiguration.objects.all()
    context = {
        "emailconfigs": emailconfigs_,
        "total_configs": emailconfigs_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/emails/emailconfigs.html', context=context)


# Locations
@admin_only
def counties(request):
    counties_ = County.objects.all()
    context = {
        "counties": counties_,
        "total_counties": counties_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/locations/counties.html', context=context)


@admin_only
def constituencies(request):
    constituencies_ = Constituency.objects.all()
    context = {
        "constituencies": constituencies_,
        "total_constituencies": constituencies_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/locations/constituencies.html', context=context)


# Facilities
@admin_only
def conditions(request):
    conditions_ = Condition.objects.all()
    context = {
        "conditions": conditions_,
        "total_conditions": conditions_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/conditions.html', context=context)


@admin_only
def specialities(request):
    specialities_ = FacilitySpeciality.objects.all()
    context = {
        "specialities": specialities_,
        "total_specialities": specialities_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/specialities.html', context=context)


@admin_only
def service_categories(request):
    service_categories_ = ServiceCategory.objects.all()
    context = {
        "service_categories": service_categories_,
        "total_service_categories": service_categories_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/services_categories.html', context=context)


@admin_only
def services(request):
    services_ = Service.objects.all()
    context = {
        "services": services_,
        "total_services": services_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/services.html', context=context)


@admin_only
def facilities(request):
    facilities_ = Facility.objects.all()
    context = {
        "facilities": facilities_,
        "total_facilities": facilities_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/facilities.html', context=context)


@admin_only
def facility_types(request):
    facility_types_ = FacilityType.objects.all()
    context = {
        "facility_types": facility_types_,
        "total_facility_types": facility_types_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/facility_types.html', context=context)


@admin_only
def appointments(request):
    appointments_ = Appointment.objects.all()
    context = {
        "appointments": appointments_,
        "total_appointments": appointments_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/appointments.html', context=context)


@admin_only
def encounters(request):
    encounters_ = Encounter.objects.all()
    context = {
        "encounters": encounters_,
        "total_encounters": encounters_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/facilities/encounters.html', context=context)


# Shop
@admin_only
def product_categories(request):
    product_categories_ = Category.objects.all()
    context = {
        "product_categories": product_categories_,
        "total_product_categories": product_categories_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/shop/product_categories.html', context=context)


@admin_only
def products(request):
    products_ = Product.objects.all()
    context = {
        "products": products_,
        "total_products": products_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/shop/products.html', context=context)


@admin_only
def orders(request):
    orders_ = Order.objects.all()
    context = {
        "orders": orders_,
        "total_orders": orders_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/shop/orders.html', context=context)


def blogs(request):
    blogs_ = Blog.objects.all()
    context = {
        "blogs": blogs_,
        "total_blogs": blogs_.count(),
    }
    return render(request, template_name='super-admin-dashboard/pages/blogs/blogadmin.html', context=context)


def new_blog(request):
    context = {"tags": Tag.objects.all()}
    if request.method == 'POST':
        tags = Tag.objects.filter(id__in=request.POST.getlist('tags'))

        blog = Blog.objects.create(
            created_by=request.user,
            title=request.POST.get('title'),
            body=request.POST.get('body'),
            image=request.FILES.get('image')
        )
        blog.tags.set(tags)
        blog.save()
        messages.success(request, "Blog published successfully")
        return redirect('super-admin-new-blog')
    return render(request, template_name='super-admin-dashboard/pages/blogs/new-blog.html', context=context)


def update_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    context = {
        "tags": Tag.objects.all(),
        "blog": blog
    }
    if request.method == 'POST':
        blog.title = request.POST.get('title')
        blog.body = request.POST.get('body')
        blog.tags = request.POST.getlist('tags')
        image = request.POST.get('image', None)
        if image:
            blog.image = image
        blog.save()
        messages.success(request, "Blog updated successfully")
        return redirect('new-blog')
    return render(request, template_name='super-admin-dashboard/pages/blogs/update-blog.html', context=context)
