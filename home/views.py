from django.shortcuts import render
from django.views.generic import TemplateView

class ShowHomeView(TemplateView):
    template_name = 'home/index.html'

