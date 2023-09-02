from django.shortcuts import render, redirect, HttpResponse
from tablib import Dataset
from .models import AyantDroit
from .resources import AyantDroitResource
from django.contrib.auth.decorators import login_required


@login_required(login_url='accesPage')
def list_ayantdroit(request):
    ayantdroit = AyantDroit.objects.all()
    context = {'ayantdroit': ayantdroit}
    return render(request, 'ayantdroit/list_ayantdroit.html', context)


@login_required(login_url='accesPage')
def import_ayantdroit(request):
    if request.method == 'POST':
        ayantdroit_resource = AyantDroitResource
        dataset = Dataset()
        new_ayantdroits = request.FILES['my_file']
        imported_data = dataset.load(new_ayantdroits.read(), format='xlsx')
        for data in imported_data:
            value = AyantDroit(
                data[1],
                data[3],
                data[5],
                data[6],
                data[7],
                data[8],
                data[17],
            )
            value.save()
    return render(request, 'personnel/formimport.html')
