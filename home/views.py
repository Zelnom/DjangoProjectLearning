from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView


class HomeTemplateView(TemplateView):
    template_name = "home/home_page.html"
