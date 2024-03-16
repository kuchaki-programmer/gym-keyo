from django.shortcuts import render
from django.views.generic import TemplateView
from team.models import Trainer

class AboutView(TemplateView):
    template_name = 'about/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['trainers_count'] = Trainer.objects.all().count()
        return context
