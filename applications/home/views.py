from django.shortcuts import render
from django.views.generic import (
    TemplateView,
    ListView
)

class IndexView(TemplateView):
    template_name = "home/index.html"

class AboutView(TemplateView):
    template_name = "home/about.html"

