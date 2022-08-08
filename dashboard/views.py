import datetime
from django.http import JsonResponse
from django.shortcuts import redirect, render
from . import models
from pages import models as p

# Create your views here.


def dashboard(request):
    branches = models.Branches.objects.all().order_by('-date')
    context = {
        'branches': branches
    }
    return render(request, 'dashboard.html', context)


def printer(request):
    return render(request, 'printer.html')


def deleteBranch(req, id):
    models.Branches.objects.filter(id=id).delete()
    return redirect('branches')


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
    if request.method == "POST":
        branchName = request.POST['branchName']
        models.Branches.objects.create(
            name=branchName,

        )
        return redirect('branches')
    else:
        branches = models.Branches.objects.all()
        context = {
            'branches': branches
        }
        return render(request, 'branches.html', context)
