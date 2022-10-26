from multiprocessing import context
from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {
        "title": "HOME"
    }
    return render(request, 'web/home.html', context=context)
