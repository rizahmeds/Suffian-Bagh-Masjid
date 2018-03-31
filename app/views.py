# from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from app.models import UserProfile

class IndexView(TemplateView):
    template_name = "index.html"

class HomeView(TemplateView):
    template_name = "home.html"

class AboutusView(TemplateView):
    template_name = "about-us.html"

class PrayersView(TemplateView):
    template_name = "prayers.html"

class PortfolioView(TemplateView):
    template_name = "portfolio.html"

class ContactusView(TemplateView):
    template_name = "contact-us.html"

class SchoolView(TemplateView):
    template_name = "school.html"

class SignupView(TemplateView):
    template_name = "signup.html"

class DonationView(TemplateView):
    template_name = "donation.html"

    def post(self, request, *args, **kwargs):
        email = request.POST.get('email')
        username = email.split('@')[0]
        password = request.POST.get('password')

        user = User.objects.filter(email=email).first()
        if user:
            return HttpResponse('User already exists in the system. Please login instead.')

        user = User.objects.create_user(username, email, password)

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.profile.roles = [request.POST.get('role')]
        user.profile.save()
        user.save()

        login(request, user)
        return HttpResponseRedirect('/home')


class LoginView(TemplateView):
    template_name = "login.html"

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        if email:
            user = User.objects.filter(email=email).first()
            username = user.username if user else None
        user = User.objects.filter(username=username).first()

        if not user:
            return HttpResponse("User doesn't exist. Please signup and try again.")

        user = authenticate(username=username, password=password)
        if not user:
            return HttpResponse("Password incorrect. Please try again or reset password.")

        login(request, user)
        return HttpResponseRedirect('/home')
