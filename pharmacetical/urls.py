from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

app_name = 'pharmacetical'
urlpatterns = [
    path('create_pharmacy', create_pharmacy, name='create_pharmacy'),
    path('dashboard', pharmacy_dashboard, name='dashboard'),
    path('upload-product', upload_product, name='upload-product'),
    path('create-product', create_product, name='create-product'),
    path('live-product', live_product, name='live-product'),
    path('pending-product', pending_product, name='pending-product'),
    path('approved-product', approved_product, name='approved-product'),
    path('unapproved-product', unapproved_product, name='unapproved-product'),
    path('pending-orders', pending_orders, name='pending-orders'),
    path('confirmed-orders', confirmed_orders, name='confirmed-orders'),
    path('product-detail', product_detail, name='product-detail'),
    path('pharmacy-report', pharmacy_report, name='pharmacy-report'),
    path('send_order_email', send_order_email, name='send_order_email'),
    path('prescription-orders', prescription_orders, name='prescription-orders'),
    
]
