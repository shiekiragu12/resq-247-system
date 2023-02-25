from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers
from rest_framework_swagger.views import get_swagger_view
from .views import *

router = routers.DefaultRouter()
router.register(r'profiles', ProfileViewSet)
router.register(r'users', UserViewSet)
router.register(r'product-categories', ProductCategoryViewSet)
router.register(r'products', ProductViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'counties', CountyViewSet)
router.register(r'constituencies', ConstituencyViewSet)
router.register(r'conditions', ConditionViewSet)
router.register(r'specialities', SpecialityViewSet)
router.register(r'facilities', FacilityViewSet)
router.register(r'qualifications', QualificationViewSet)
router.register(r'doctors', DoctorViewSet)
router.register(r'patients', PatientViewSet)
router.register(r'staff', StaffViewSet)
router.register(r'service-categories', ServiceCategoryViewSet)
router.register(r'services', ServiceViewSet)
router.register(r'appointments', AppointmentViewSet)
router.register(r'encounters', EncounterViewSet)

schema_view = get_swagger_view(title='Resq247 API')

urlpatterns = [
    path('', include(router.urls)),
    path('docs/', schema_view, name='api-docs'),
    # path('docs/', TemplateView.as_view(
    #     template_name='swagger.html',
    #     extra_context={'schema_url': 'openapi-schema'}
    # ), name='swagger-ui')
]
