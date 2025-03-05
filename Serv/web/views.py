from django.shortcuts import render
from random import randint

def random(request):
    val = randint(1000,9999)
    context = {'val': val}
    return render(request, 'index.html', context)
