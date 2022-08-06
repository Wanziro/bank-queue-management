from django.shortcuts import redirect, render
from . import models

# Create your views here.


def dashboard(request):
    branches = models.Branches.objects.all().order_by('-date')
    context = {
        'branches': branches
    }
    return render(request, 'dashboard.html', context)


def deleteBranch(req, id):
    models.Branches.objects.filter(id=id).delete()
    return redirect('branches')


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
