from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class Home(TemplateView):
    template_name = 'index.html'


class About(TemplateView):
    template_name = 'about.html'


class Login(TemplateView):
    template_name = 'login.html'


class Feedback(TemplateView):
    template_name = 'feedback.html'


class Queue(TemplateView):
    template_name = 'queue.html'


class Dashboard(TemplateView):
    template_name = 'dashboard.html'
