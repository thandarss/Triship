"""
Definition of views.
"""

from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpRequest

def home(request):
    return render(request, 'home.html',{'name':'Petrichor'})

def add(request):
    var1 = int(request.POST['num1'])
    var2 = int(request.POST['num2'])
    res = var1 + var2
    return render(request, 'result.html', {'result':res})

#def add(request):
#    var1 = int(request.GET['num1'])
#    var2 = int(request.GET['num2'])
#    res = var1 + var2
#    return render(request, 'result.html', {'result': res})


