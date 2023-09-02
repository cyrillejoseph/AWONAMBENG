from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='accueil'),
    # path('ajout_employe', views.ajouter_employe, name='ajout_employe'),
    # path('ajout_ddebpc', views.ajouter_ddebpc, name='ajout_ddebpc'),
    # path('modif_ddebpc/<str:pk>', views.modifier_ddebpc, name='modif_ddebpc'),
    # path('suppr_ddebpc/<str:pk>', views.supprimer_ddebpc, name='suppr_ddebpc'),
]
