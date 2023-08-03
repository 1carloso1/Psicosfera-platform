from django.shortcuts import render
from django.views.generic import TemplateView
class Home(TemplateView):
    template_name = 'home.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)