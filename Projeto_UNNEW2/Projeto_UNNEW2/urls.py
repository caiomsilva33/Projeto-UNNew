from django.contrib import admin
from django.urls import path
from .views import inicio, cursos

urlpatterns = [
    path('', inicio, name='inicio'),
    path('cursos/', cursos, name='cursos'),
    path('admin/', admin.site.urls),
]
