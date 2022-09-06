from tkinter.font import names
from django.views.generic import TemplateView
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
import datetime
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from dashboard import models as dashboardmodels
from dashboard import models
from .models import NotificationRequest, QueueDetails
from dashboard.models import Branches


# Create your views here.


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("/")


def home(request):
    branches = Branches.objects.all().order_by('date')[:5]
    context = {
        'branches': branches,
    }
    return render(request, 'index.html', context)


class About(TemplateView):
    template_name = 'about.html'


def login_request(request):
    if request.user.is_authenticated:
        return redirect('/dashboard')
    else:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(request, user)
                    # messages.info(
                    #     request, f"You are now logged in as {username}")
                    return redirect('/dashboard')
                else:
                    messages.warning(
                        request, "Invalid username or password. Try again later")
            else:
                messages.warning(
                    request, "Invalid username or password. Try again later")

        form = AuthenticationForm()
        users = User.objects.all()
        return render(request, 'login.html', {'form': form, 'users': users})


def register(req):
    if req.user.is_authenticated:
        return redirect('/dashboard')
    else:
        users = User.objects.all()
        if len(users) == 0:
            if req.method == 'POST':
                form = UserCreationForm(req.POST)
                if form.is_valid():
                    form.save()
                    username = form.cleaned_data.get('username')
                    raw_password = form.cleaned_data.get('password1')
                    user = authenticate(username=username,
                                        password=raw_password)
                    login(req, user)
                    return redirect('/dashboard')
            else:
                form = UserCreationForm()
            return render(req, 'register.html', {'form': form})
        else:
            return redirect("/login")


def feedback(request):
    if request.method == 'POST':
        names = request.POST['names']
        email = request.POST['email']
        phone = request.POST['phone']
        comment = request.POST['comment']
        dashboardmodels.Feedbacks.objects.create(
            customer_full_name=names,
            email_address=email,
            phone_number=phone,
            message=comment
        )
        messages.success(
            request, "Your feedback has been submitted successfully! we will get back to you if necessary")
        return redirect('/feedback')
    return render(request, 'feedback-form.html')


def notificationReq(request):
    if request.method == 'GET':
        length = request.GET['length']
        names = request.GET['names']
        phone = request.GET['phone']
        NotificationRequest.objects.create(
            names=names,
            phone=phone,
            queueLength=length
        )
        return JsonResponse({'msg': 'Request was success'})
    return JsonResponse({'msg': 'Error'})


def queue_request(req, id):
    branch = models.Branches.objects.get(id=id)
    return render(req, 'queue.html', {
        "branch": branch
    })


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


class GetChartData(View):
    def get(self, request):
        day = datetime.datetime.now().day
        month = datetime.datetime.now().month
        year = datetime.datetime.now().year

        clients = QueueDetails.objects.filter(
            day=day,
            month=month,
            year=year,
            status="served"
        )
        if len(clients) > 0:
            return JsonResponse([client.serialize() for client in clients], safe=False)
        else:
            clients = QueueDetails.objects.filter(
                month=month,
                year=year,
                status="served"
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


class GetAllBranches(View):
    def get(self, request):
        branches = Branches.objects.all()
        return JsonResponse([branch.serialize() for branch in branches], safe=False)
