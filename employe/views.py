from django.shortcuts import render, redirect
from .models import Employe
from .forms import EmployeForm
from ddebpc.filters import DdeBpcFiltre
from django.contrib.auth.decorators import login_required


@login_required(login_url='accesPage')
def list_employe(request):
    form = EmployeForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {'form': form, 'dataEmploye': Employe.objects.all()}
    return render(request, 'employe/list_employe.html', )


@login_required(login_url='accesPage')
def detail_employe(request, pk):
    employe = Employe.objects.get(id=pk)
    ddebpc = employe.ddebpc_set.all()
    ddebpc_total = ddebpc.count()
    myfilter = DdeBpcFiltre(request.GET, queryset=ddebpc)
    ddebpc = myfilter.qs
    context = {'employe': employe, 'ddebpc': ddebpc, 'ddebpc_total': ddebpc_total, 'myFilter': myfilter}
    return render(request, 'employe/detail_employe.html', context)
