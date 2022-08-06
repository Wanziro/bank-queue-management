from django.shortcuts import render
from . import models

# Create your views here.


def dashboard(request):
    branches = models.Branches.objects.all().order_by('-date')
    context = {
        'branches': branches
    }
    return render(request, 'dashboard.html', context)
