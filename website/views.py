from django.shortcuts import render
import string
from facilities.models import Condition

# Colors - Cyan blue,


# Create your views here.
def index_view(request):
    return render(request, 'index.html')


def index(request):
    return render(request, 'index.html', {})


def signin(request):
    return render(request, 'auth/signin.html', {})


def signup(request):
    return render(request, 'auth/sign-up.html', {})


# Services nav-links
def service(request):
    return render(request, 'services/services.html', {})


def emergencies(request):
    return render(request, 'services/emergencies.html', {})


def birthingcare(request):
    return render(request, 'services/birthing-care.html', {})


def cancercare(request):
    return render(request, 'services/cancer-care.html', {})


def familymedicine(request):
    return render(request, 'services/family-medicine.html', {})


def emergencymedicine(request):
    return render(request, 'services/emergency-medicine.html', {})


def laboratiescenter(request):
    return render(request, 'services/laboraties-center.html', {})


def onlinereferral(request):
    return render(request, 'services/online-referral.html', {})


def firstaid(request):
    return render(request, 'services/first-aid.html', {})


# about
def about(request):
    return render(request, 'about.html', {})


# Health in Hand
def health(request):
    return render(request, 'health/health.html', {})


def diseaselist(request):
    starts_with = request.GET.get('letter', 'a')
    context = {
        "letters": string.ascii_lowercase,
        "conditions": Condition.objects.filter(name__startswith=starts_with)
    }
    return render(request, 'health/disease-list.html', context)


def healthtopic(request):
    return render(request, 'health/health-topic.html', {})


def healthyliving(request):
    return render(request, 'health/healthy-living.html', {})


def location(request):
    return render(request, 'health/medical-facilities.html', {})


def teams(request):
    return render(request, 'teams.html', {})


def project(request):
    return render(request, 'health/project.html', {})


def projectdetails(request):
    return render(request, 'health/project-details.html', {})


def faq(request):
    return render(request, 'health/faq.html', {})


def appointment(request):
    return render(request, 'health/appointment.html', {})


def testimonials(request):
    return render(request, 'health/testimonials.html', {})


def howitworks(request):
    return render(request, 'health/how-it-works.html', {})


def termsconditions(request):
    return render(request, 'health/terms-conditions.html', {})


def privacypolicy(request):
    return render(request, 'health/privacy-policy.html', {})


# solution
def solution(request):
    return render(request, 'solution.html', {})


def blog(request):
    return render(request, 'blog.html', {})


def contact(request):
    return render(request, 'contact.html', {})


# shop
def shop(request):
    return render(request, 'shop/shop.html', {})


def allergy(request):
    return render(request, 'shop/allergy-medicine.html', {})


def prescription(request):
    return render(request, 'shop/refill-prescription.html', {})


def mobileaid(request):
    return render(request, 'shop/mobile-aid.html', {})


def medicaldevices(request):
    return render(request, 'shop/medical-devices.html', {})


def prescriptionmedication(request):
    return render(request, 'shop/prescription-medication.html', {})


def nutraceuticals(request):
    return render(request, 'shop/nutraceuticals.html', {})


# locations
def eldoret(request):
    return render(request, 'locations/eldoret.html', {})


def embu(request):
    return render(request, 'locations/embu.html', {})


def kisumu(request):
    return render(request, 'locations/kisumu.html', {})


def machakos(request):
    return render(request, 'locations/machakos.html', {})


def mombasa(request):
    return render(request, 'locations/mombasa.html', {})


def nairobi(request):
    return render(request, 'locations/nairobi.html', {})


def nakuru(request):
    return render(request, 'locations/nakuru.html', {})


def nyeri(request):
    return render(request, 'locations/nyeri.html', {})


# solutions
def analytic(request):
    return render(request, 'solution/analytic_service.html', {})


def emergency(request):
    return render(request, 'solution/emergency.html', {})


def equip(request):
    return render(request, 'solution/healthcare_equip.html', {})


def healthcare(request):
    return render(request, 'solution/healthcare_services.html', {})


def medcommerce(request):
    return render(request, 'solution/med_ecommerce.html', {})


def telehealth(request):
    return render(request, 'solution/telehealth.html', {})


def medicare(request):
    return render(request, 'solution/medicare.html', {})
