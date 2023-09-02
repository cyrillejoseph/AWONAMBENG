from django.shortcuts import render, redirect
from personnel.models import Personnel
from ayantdroit.models import AyantDroit
from ddebpc.models import DdeBpc
# from identpatient.models import IdentPatient
# from .forms import DdeBpcForm, EmployeForm
from django.contrib.auth.decorators import login_required


@login_required(login_url='accesPage')
def home(request):
    personnels = Personnel.objects.all()
    ayantdroits = AyantDroit.objects.all()
    ddebpcs = DdeBpc.objects.all()
    context = {'personnels': personnels, 'ayantdroits': ayantdroits, 'ddebpcs': ddebpcs}
    return render(request, 'ddebpc/accueil.html', context)
