from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.

def faq1(request):
    
    template = loader.get_template('faq1.html')
    context = {}
    
    return HttpResponse(template.render(context, request))

