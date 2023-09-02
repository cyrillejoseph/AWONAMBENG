from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ddebpc.urls')),
    path('personnel/', include('personnel.urls')),
    path('employe/', include('employe.urls')),
    path('ayantdroit/', include('ayantdroit.urls')),
    path('compte/', include('compte.urls')),
]
