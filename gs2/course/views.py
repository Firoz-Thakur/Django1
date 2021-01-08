from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def learn_hm(request):
 return HttpResponse('Home page')

def learn_dj(request):
 return HttpResponse('hqhello daango guru')

def learn_py(request):
 a='hello daango guru'
 return HttpResponse(a)

def learn_math(request):
 b=10+10
 return HttpResponse(b)
