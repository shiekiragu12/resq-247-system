from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

urlpatterns = [
    path("blogs/", blogs, name="blogs"),
    path("blogs/<str:blog_id>/<str:slug>/", single_blog, name="single_blog"),
    path("blogs/<str:blog_id>/", blog_reply, name="blog_reply"),
]
