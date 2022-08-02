import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View
from .models import QueueDetails

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


class GetClientsOnTheQueue(View):
    def get(self, request):
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

        clients = QueueDetails.objects.filter(
            day=day,
            month=month,
            year=year,
            status="online"
        )
        return JsonResponse([client.serialize() for client in clients], safe=False)


class AddClientToTheQueue(View):
    def get(self, request):
        day = request.GET.get('day')
        month = request.GET.get('month')
        year = request.GET.get('year')
        jsonDate = request.GET.get('jsonDate')

        obj = QueueDetails.objects.create(
            day=day,
            month=month,
            year=year,
            joinedTimeAndDate=jsonDate
        )
        print("Client obj ", obj)
        return JsonResponse({'msg': 'Client added successfull'})


class UpdateClient(View):
    def get(self, request):
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year
        sdate = request.GET.get('sd')

        clients = QueueDetails.objects.filter(
            day=day,
            month=month,
            year=year,
            status="online"
        )

        for client in clients:
            print('client details ', client)
            QueueDetails.objects.filter(
                id=client.id).update(status="served", leaveTimeAndDate=sdate)
            break

        return JsonResponse({'msg': 'Client updated successfull'})
