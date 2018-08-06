from django.shortcuts import render
from django.template.context_processors import request
from django.http import HttpResponse

# Create your views here.
def login_page(request):
    return HttpResponse('<h1>hello</h1>')

