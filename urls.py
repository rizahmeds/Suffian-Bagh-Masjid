
from django.urls import path

from django.contrib import admin
from django.views.generic import TemplateView
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),
    path('home', HomeView.as_view(), name='home'),
    path('signup', SignupView.as_view(), name='signup'),
    path('login', LoginView.as_view(), name='login'),
    path('about-us', AboutusView.as_view(), name='about-us'),
    path('prayers', PrayersView.as_view(), name='prayers'),
    path('portfolio', PortfolioView.as_view(), name='portfolio'),
    path('contact-us', ContactusView.as_view(), name='contact-us'),
    path('school', SchoolView.as_view(), name='school'),
    path('donation', DonationView.as_view(), name='donation'),
]
