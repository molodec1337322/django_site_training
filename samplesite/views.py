from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.template import loader
from django.views.generic.edit import CreateView, FormView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.contrib import auth
import os


class RegistrationFormView(FormView):
    form_class = UserCreationForm

    # Ссылка, на которую будет перенаправляться пользователь в случае успешной регистрации.
    # В данном случае указана ссылка на страницу входа для зарегистрированных пользователей.
    success_url = "/login/"
    template_name = "samplesite/register.html"
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        # Создаём пользователя, если данные в форму были введены корректно.
        form.save()

        # Вызываем метод базового класса
        return super(RegisterFormView, self).form_valid(form)


class LoginFormView(FormView):

    form_class = AuthenticationForm
    template_name = 'samplesite/login.html'
    success_url = '/'
    success_url = reverse_lazy('index')

    def form_valid(self, form):

        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)


class LogoutView(View):

    def get(self, request):

        logout(request)
        return HttpResponseRedirect('/')


def index(request):

    return render(request, 'samplesite/index_general.html')


