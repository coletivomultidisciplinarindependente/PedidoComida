from django.shortcuts import render
from django.views.generic import View
from django.shortcuts import render


from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

from django.contrib.auth.models import User

from .forms import *
from .models import *
# Create your views here.




class Index(View):

	def get(self, request):

		user = request.user

		if user.is_authenticated:
			return render(
				request,
				'index.html',
				context={},
			)
			# return HttpResponseRedirect("/")

		return render(
			request,
			'indexpublica.html',
			context={},
		)


class RestauranteView(View):

	def get(self, request, rest_id):

		restaurante = Restaurante.objects.get(id=rest_id)

		classes = ClasseDeProdutos.objects.filter(restaurante=restaurante)



		return render(
			request,
			'restaurante_pagina_inicial.html',
			context={'restaurante': restaurante, 'classes': classes},
		)


class Login(View):

	def get(self, request):

		user = request.user

		if user.is_authenticated:
			return HttpResponseRedirect("/")

		return render(
			request,
			'login.html',
			context={},
		)

	def post(self, request):
	

		form = LoginForm(request.POST)

		if form.is_valid():
		    userObj = form.cleaned_data
		    email = userObj['email']
		    password = userObj['password']

		    # perfil = Perfil.objects.filter(user__username= email).first()

		#     # if perfil.inativo:
		#     #     return render(request, 'login.html', {'error': "Usuário inativo"})

		    user = authenticate(request, username=email, password=password)

		    if user is not None:
		        login(request, user)
		        return HttpResponseRedirect("/")
		    else:
		        return render(
		            request,
		            'login.html',
		            context={ 'error': "Usuário não encontrado ou Senha errada"
		            },
		        )
		else:
		    campo_obrigatorio = []
		    for k in list(form.errors.keys()):
		        campo_obrigatorio.append(k)



		    return render(request, 'login.html',
		        context={'erro_formulario': campo_obrigatorio})





class Logout(View):

	def get(self, request):
		logout(request)
		return HttpResponseRedirect("/")


