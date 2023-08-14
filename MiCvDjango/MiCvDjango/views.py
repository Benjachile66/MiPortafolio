from django.shortcuts import render , redirect
from django.conf import settings
import os
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.utils.translation import activate
from django.utils import translation

from django.urls import reverse


def home(request):
	print("Vengo de home view")
	Retorno = Get_lenguage("home.html","home",request)
	context = Retorno[1]
	template_name = Retorno[0]
	print(Retorno)
	return render(request , template_name , context)

def proyectos(request):
	Retorno = Get_lenguage("Proyectos.html","proyectos",request)	
	context = Retorno[1]
	template_name = Retorno[0]
	print(Retorno)
	return render(request , template_name , context)

def Mesa_de_ayuda(request):
	Retorno = Get_lenguage('Mesa_de_ayuda.html',"Mesa_de_ayuda",request)
	context = Retorno[1]
	template_name = Retorno[0]
	return render(request, template_name , context)

def cv(request):
	Retorno = Get_lenguage('micv.html',"cv",request)
	context = Retorno[1]
	template_name = Retorno[0]
	return render(request, template_name , context)


# Cambiar idioma :

def switch_language(request, language_code):
	#print("Vengo de swtichlengauej")
	if language_code == 'en':  # Si el código de idioma es 'en' (ingles)
		translation.activate('en')  # Establece el idioma activo como ingles
		request.session['preferred_language'] = 'en'
		#language_code = request.session.get('preferred_language', 'es')
		#print(language_code)
	elif language_code == 'favicon.ico':
			print("ERROR , VER PORQUE LLEGO ACA CON FAVICON.ICO")
			HttpResponse("fin")
	else:
		translation.activate('es')  # De lo contrario, establece el idioma activo como español
		request.session['preferred_language'] = 'es'	
		#request.session['preferred_language'] = 'es'
	#print(request.session.get('preferred_language', 'es'))
	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
	#return redirect(reverse('home'))

def Get_lenguage(NombreHtml, active_page,request):
    # Obtiene el código de idioma actual
    #language_code = translation.get_language()
    language_code = request.session.get('preferred_language', 'es')
    # Comprueba si el idioma es inglés ('en') o español ('es')
    template_name = NombreHtml  # Si es español, usa el nombre de la plantilla sin cambios
    if language_code == 'en':
        template_name = 'eng/' + NombreHtml  # Si es inglés, agrega 'eng/' al nombre de la plantilla
    
    # Crea un diccionario de contexto con la página activa y el código de idioma
    context = {'active_page': active_page, 'language_code': language_code}

    # Crea una lista que contiene el nombre de la plantilla y el contexto
    retorno = [template_name, context]

    # Devuelve la lista
    return retorno
