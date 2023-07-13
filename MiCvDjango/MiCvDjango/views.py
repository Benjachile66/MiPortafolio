from django.shortcuts import render
from django.conf import settings
import os
from django.http import HttpResponse

def home(request):
	direccion = str( settings.BASE_DIR /'PlantillasHTML'/'home.html')
	context = {'active_page': 'home'}
	return render(request , 'home.html' , context)
	#return "HolaMundo"
	#return HttpResponse(direccion)

def proyectos(request):
	direccion = str( settings.BASE_DIR  /'PlantillasHTML'/'Proyectos.html') 
	context = {'active_page': 'proyectos'}
	return render(request , 'Proyectos.html',context)

def Mesa_de_ayuda(request):
	direccion = str( settings.BASE_DIR  /'PlantillasHTML'/'Mesa_de_ayuda.html')
	context = {'active_page' : 'Mesa_de_ayuda'}
	return render(request, 'Mesa_de_ayuda.html' , context)

