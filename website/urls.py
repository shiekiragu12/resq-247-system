from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    # path('', RedirectView.as_view(url='index')),
    path('', views.index,  name="index"),
    # path('sign-in', views.signin, name="signin"),
    # path('sign-up', views.signup, name="signup"),
    
    # services paths
    path('service', views.service, name="service"),
    path('services/emergencies', views.emergencies, name="emergencies"),
    path('birthing-care', views.birthingcare, name="birthing-care"),
    path('cancer-care', views.cancercare, name="cancer-care"),
    path('family-medicine', views.familymedicine, name="family-medicine"), 
    path('emergency-medicine', views.emergencymedicine, name="emergency-medicine"),
    path('laboraties-center', views.laboratiescenter, name="laboraties-center"),
    path('online-referral', views.onlinereferral, name="online-referral"),
    path('first-aid', views.firstaid, name="first-aid"),
    
    # about
    path('about', views.about, name="about"),
    
    # Health in Hand
    path('health', views.health, name="health"),
    path('disease-list', views.diseaselist, name="disease-list"),
    path('health-topic', views.healthtopic, name="health-topic"),
    path('healthy-living', views.healthyliving, name="healthy-living"),
    path('location', views.location, name="location"),
    path('teams', views.teams, name="teams"),
    path('project', views.project, name="project"),
    path('project-details', views.projectdetails, name="project-details"),
    path('faq', views.faq, name="faq"),
    path('appointment', views.appointment, name="appointment"),
    path('testimonials', views.testimonials, name="testimonials"),
    path('how-it-works', views.howitworks, name="how-it-works"),
    path('terms-conditions', views.termsconditions, name="terms-conditions"),
    path('privacy-policy', views.privacypolicy, name="privacy-policy"),

    # solution
    path('solution', views.solution, name="solution"),
    path('blog', views.blog, name="blog"),
    path('contact', views.contact, name="contact"),
    
    # shop
    path('shop', views.shop, name="shop"),
    path('refill-prescription', views.prescription, name="refill-prescription"),
    path('allergy-medicine', views.allergy, name="allergy-medicine"),
    path('mobile-aid', views.mobileaid, name="mobile-aid"),
    path('medical-devices', views.medicaldevices, name="medical-devices"),
    path('prescription-medication', views.prescriptionmedication, name="prescription-medication"),
    path('nutraceuticals', views.nutraceuticals, name="nutraceuticals"),
    
    #locations
    path('eldoret', views.eldoret, name="eldoret"),
    path('embu', views.embu, name="embu"),
    path('kisumu', views.kisumu, name="kisumu"),
    path('machakos', views.machakos, name="machakos"),
    path('mombasa', views.mombasa, name="mombasa"),
    path('nairobi', views.nairobi, name="nairobi"),
    path('nakuru', views.nakuru, name="nakuru"),
    path('nyeri', views.nyeri, name="nyeri"),
    
    #solution
    path('analytic', views.analytic, name="analytic"),
    path('emergency', views.emergency, name="emergency"),
    path('equip', views.equip, name="equip"),
    path('healthcare', views.healthcare, name="healthcare"),
    path('medcommerce', views.medcommerce, name="medcommerce"),
    path('telehealth', views.telehealth, name="telehealth"),
    path('medicare', views.medicare, name="medicare"),

]
