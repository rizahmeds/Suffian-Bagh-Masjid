
from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^home', HomeView.as_view(), name='home'),
    url(r'^signup', SignupView.as_view(), name='signup'),
    url(r'^login', LoginView.as_view(), name='login'),
    url(r'^about-us', AboutusView.as_view(), name='about-us'),
    url(r'^prayers', PrayersView.as_view(), name='prayers'),
    url(r'^portfolio', PortfolioView.as_view(), name='portfolio'),
    url(r'^contact-us', ContactusView.as_view(), name='contact-us'),
    url(r'^school', SchoolView.as_view(), name='school'),
    url(r'^donation', DonationView.as_view(), name='donation'),
]
