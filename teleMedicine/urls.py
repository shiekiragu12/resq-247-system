from django.contrib import admin

from . import settings
from django.contrib.staticfiles.urls import static
from django.urls import path, include
from superadmin.decorators import admin_only

urlpatterns = [
  path('admin/', admin.site.urls),
  path('dashboard/super/admin/', include('superadmin.urls')),

  # Main website urls like homepage, about, contact, etc
  path('', include('website.urls')),
  path('', include('mainapp.urls')),

  # Api urls including the docs url which is /api/docs/
  path('api/', include('api.urls')),

  # Rest of application urls
  path('facilities/', include('facilities.urls')),
  path('shop/', include('shop.urls')),
  path('account/', include('account.urls')),
  path('tracking/', include('tracking.urls')),
  path('pharmacetical/', include('pharmacetical.urls')),
  path('patient/', include('patient.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_URL) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
