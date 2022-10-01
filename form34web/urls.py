from django.urls import re_path, path, include
from rest_framework import routers
from form34web import views

router = routers.DefaultRouter()
router.register('regions', viewset=views.RegiontViewSet)
router.register('pdf_paths', viewset=views.PdfpathViewSet)

urlpatterns = [
    path('', include(router.urls)),
]