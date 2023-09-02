from django.urls import path
from . import views

urlpatterns = [
    path('liste', views.list_ayantdroit, name='list_aydrt'),
    path('import', views.import_ayantdroit, name='import_aydrt'),
]
