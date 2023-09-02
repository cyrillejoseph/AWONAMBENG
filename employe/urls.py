from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_employe, name='employe'),
    path('<str:pk>', views.detail_employe, name='detail_employe'),
]
