from django.urls import path
from .views import *

urlpatterns = [
    path('', dashboard, name='super-admin'),

    # Users
    path('users/', users, name='super-admin-users'),
    path('doctors/', doctors, name='super-admin-doctors'),
    path('staff/', staff, name='super-admin-staff'),
    path('patients/', patients, name='super-admin-patients'),

    # Emails and email settings
    path('emails/', emails, name='super-admin-emails'),
    path('emails/configurations/', emailconfigs, name='super-admin-emailconfigs'),

    # Location - counties & constituencies
    path('counties/', counties, name='super-admin-counties'),
    path('constituencies/', constituencies, name='super-admin-constituencies'),

    # Facilities
    path('facilities/', facilities, name='super-admin-facilities'),
    path('facilities/types/', facility_types, name='super-admin-facility_types'),
    path('conditions/', conditions, name='super-admin-conditions'),
    path('specialities/', specialities, name='super-admin-specialities'),
    path('services-categories/', service_categories, name='super-admin-service_categories'),
    path('services/', services, name='super-admin-services'),
    path('appointments/', appointments, name='super-admin-appointments'),
    path('patient-medical-data/', encounters, name='super-admin-encounters'),

    # Shop
    path('products/', products, name='super-admin-products'),
    path('product-categories/', product_categories, name='super-admin-product_categories'),
    path('orders/', orders, name='super-admin-orders'),

    # Blogs
    path('blogs/', blogs, name='super-admin-blogs'),
    path('blogs/new-blog/', new_blog, name='super-admin-new-blog'),
    path('blogs/update/<str:blog_id>/', update_blog, name='super-admin-blog-update'),
]
