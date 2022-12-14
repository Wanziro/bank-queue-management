import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from . import models
from pages import models as p

# Create your views here.


def dashboard(request):
    if request.user.is_authenticated:
        branches = models.Branches.objects.all().order_by('-date')
        context = {
            'branches': branches
        }
        return render(request, 'dashboard.html', context)
    else:
        return redirect('/login')


def printer(request):
    if request.user.is_authenticated:
        return render(request, 'printer.html')
    else:
        return redirect('/login')


def deleteBranch(req, id):
    if req.user.is_authenticated:
        models.Branches.objects.filter(id=id).delete()
        return redirect('branches')
    else:
        return redirect('/login')


def deleteFeedBack(req, id):
    if req.user.is_authenticated:
        models.Feedbacks.objects.filter(id=id).delete()
        return redirect('feedbacks')
    else:
        return redirect('/login')


def editBranch(req, id):
    if req.user.is_authenticated:
        if req.method == "POST":
            branchName = req.POST['branchName']
            lat = req.POST['lat']
            long = req.POST['long']
            address = req.POST['address']
            id = req.POST['id']
            models.Branches.objects.filter(
                id=id
            ).update(name=branchName,
                     lat=lat,
                     long=long,
                     address=address)
            return redirect('branches')
        else:
            branch = models.Branches.objects.get(id=id)
            print(branch)
            context = {
                'branch': branch
            }
            return render(req, 'edit-branch.html', context)
    else:
        return redirect('/login')


def queue(req):
    if req.method == "POST":
        if 'day' in req.POST and 'month' in req.POST and 'year' in req.POST:
            day = req.POST['day']
            month = req.POST['month']
            year = req.POST['year']
            clients = p.QueueDetails.objects.filter(
                day=day,
                month=month,
                year=year
            ).order_by('-id')
            return JsonResponse([client.serialize() for client in clients], safe=False)
        else:
            if 'month' in req.POST:
                month = req.POST['month']
            else:
                month = datetime.datetime.now().month
            year = datetime.datetime.now().year
            clients = p.QueueDetails.objects.filter(
                month=month,
                year=year
            ).order_by('-id')
            return JsonResponse([client.serialize() for client in clients], safe=False)
    else:
        return JsonResponse({'msg': 'Invalid request'})


def branches(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            branchName = request.POST['branchName']
            lat = request.POST['lat']
            long = request.POST['long']
            address = request.POST['address']
            models.Branches.objects.create(
                name=branchName,
                lat=lat,
                long=long,
                address=address

            )
            return redirect('branches')
        else:
            branches = models.Branches.objects.all()
            context = {
                'branches': branches
            }
            return render(request, 'branches.html', context)
    else:
        return redirect('/login')


def feedbacks(request):
    if request.user.is_authenticated:
        feedbacks = models.Feedbacks.objects.all()
        context = {
            'feedbacks': feedbacks
        }
        return render(request, 'feedbacks.html', context)
    else:
        return redirect('/login')
