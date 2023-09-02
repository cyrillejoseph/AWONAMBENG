from django.shortcuts import render, redirect, HttpResponse
from tablib import Dataset
from .models import Personnel
from .resources import PersonnelResource
from django.contrib.auth.decorators import login_required


@login_required(login_url='accesPage')
def list_personnel(request):
    personnel = Personnel.objects.all()
    context = {'personnel': personnel}
    return render(request, 'personnel/list_personnel.html', context)


@login_required(login_url='accesPage')
def import_personnel(request):
    if request.method == 'POST':
        personnel_resource = PersonnelResource
        dataset = Dataset()
        new_personnels = request.FILES['my_file']
        imported_data = dataset.load(new_personnels.read(), format='xlsx')
        for data in imported_data:
            value = Personnel(
                data[2],
                data[3],
                data[4],
                data[5],
                data[6],
                data[7],
                data[8],
                data[9],
            )
            value.save()
    return render(request, 'personnel/formimport.html')
