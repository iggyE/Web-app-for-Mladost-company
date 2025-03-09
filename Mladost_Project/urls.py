"""
URL configuration for Mladost_Project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Base_App.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',PocetnaView, name='pocetna'),
    path('proizvodnja',ProizvodnjaView,name='proizvodnja'),
    path('nabavljanje-gline',NabavljanjeGlineView,name='nabavljanje-gline'),
    path('o-nama',NamaView,name='nama'),
    path('kontakt/',KontaktView,name='kontakt'),
    path('ko-smo-mi',KoSmoMiView,name='ko-smo-mi'),
    path('istorija',IstorijaView,name='istorija'),
    path('gde-se-nalazimo',GdeSeNalazimoView,name='gde-se-nalazimo'),
    path('kontakt',KontaktiView,name='kontakti'),
    path('primarna-obrada',PrimarnaObradaView,name='primarna-obrada'),
    path('sekundarna-obrada',SekundarnaObradaView,name='sekundarna-obrada'),
    path('oblikovanje-crepa',OblikovanjeCrepaView,name='oblikovanje-crepa'),
    path('susenje-slaganje',SusenjeSlaganjeView,name='susenje-slaganje'),
    path('pecenje-pakovanje',PecenjePakovanjeView,name='pecenje-pakovanje'),
    path('proba',ProbaView,name='proba')
    ]
#if settings.DEBUG:
 #   urlpatterns += static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)
  #  urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
