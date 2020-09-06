from django.shortcuts import render
from django.http import HttpResponse
from .models import Extentions
from .forms import ExtentionsForm
from django import forms


def index(request):
    form = ExtentionsForm()

    return render(request, 'base.html', {'name': 'ahmed', 'form': form})

# Create your views here.


def add(request):
    if request.method == 'POST':
        form = ExtentionsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            print('-_'*100)
            print(form.is_valid())
            print(form.errors)
            return render(request, 'base.html')

        else:
            print('*'*100)
            print(form.is_valid())
            print(form.errors)
            print('#'*100)
            for errors in form.errors:
                print(errors)

    else:
        form = ExtentionsForm()

    return render(request, 'base.html')
