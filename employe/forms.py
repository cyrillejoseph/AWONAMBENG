from django.forms import ModelForm
from .models import Employe


class EmployeForm(ModelForm):
    class Meta:
        model = Employe
        fields = '__all__'
