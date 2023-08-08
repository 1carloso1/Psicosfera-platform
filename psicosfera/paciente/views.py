from django.shortcuts import render
from django.views.generic import TemplateView

class PerfilView(TemplateView):
    template_name = 'users-profile.html'
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
