from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from blog.forms import ContactForm
from django.core.urlresolvers import reverse


def index(request):
    context={}
    if request.method =='POST':
        VistaContacto(request)
    else:
    #Si no es post es una carga normal y continua el flujo
        return render(request, 'index.html',context)

def VistaContacto(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        print('si es un post')
        if form.is_valid():
            print('si es valido')
            form.save(commit=True)
            print('si se ha salvado')

            return HttpResponseRedirect(reverse('index'))

        else:
            print(form.errors)
    else:
        print('no es unn post')
        return render(request,'index.html')
