from django.urls import path
from . import views

urlpatterns = [
    path('liste', views.list_personnel, name='list_pers'),
    path('import', views.import_personnel, name='import_pers'),
]
