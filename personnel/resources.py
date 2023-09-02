from import_export import resources
from .models import Personnel


class PersonnelResource(resources.ModelResource):
    class Meta:
        model = Personnel
