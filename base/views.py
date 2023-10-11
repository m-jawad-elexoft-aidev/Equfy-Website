from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from .models import userModel
from .import forms
from . import send_mail
# Create your views here.

def faq1(request):
    
    template = loader.get_template('faq1.html')
    context = {}
    
    return HttpResponse(template.render(context, request))


def contact_us(request):
    template = loader.get_template('contact_us.html')
    form = forms.UserForm()
    if request.method == 'POST':
        form = forms.UserForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail.send(form.data)
            return redirect('contact_us')
    context = {'form': form}
    return HttpResponse(template.render(context, request))
