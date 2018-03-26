from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def index(request):
    context={}
    template = loader.get_template('corp/index.html')
    return HttpResponse(template.render(context, request))

def about(request):
    context={}
    template = loader.get_template('corp/about.html')
    return HttpResponse(template.render(context, request))

def enterprise(request):
    context={}
    template = loader.get_template('corp/enterprise.html')
    return HttpResponse(template.render(context, request))
