from django.shortcuts import render

def inicio(request):
    return render(request, 'telaprincipal.html')

def cursos(request):
    return render(request,'CURSOS-UNN.html')