# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.views.generic import TemplateView
class HomeView(TemplateView):
    template_name = 'index.html'
class JSView(TemplateView):
    template_name = 'jquery-3.3.1.min.js'
class JSNBRView(TemplateView):
    template_name = 'neighbors.json'
# Create your views here.
