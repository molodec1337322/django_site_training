from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
import os


def index(request):

    return render(request, 'samplesite/index_general.html')
