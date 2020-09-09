from django.shortcuts import redirect, render
# from django.http import HttpResponse, HttpResponseRedirect
from .models import Extentions
from .forms import ExtentionsForm, QueueForm
from django import forms
from django.contrib import messages


def index(request):
    if request.method == 'POST':
        form = ExtentionsForm(request.POST, request.FILES)

        if form.is_valid():
            form2data = {}
            form2data['name'] = request.POST['name']
            form2data['exten'] = request.POST['exten']
            form2data['optin'] = request.POST['optin']

            form2 = QueueForm(form2data)
            if form2.is_valid():

                form2.save()
            form.save()
            print('-_'*100)
            print(form.is_valid())
            form.cleaned_data['exten']
            form.cleaned_data['file']
            print(form.errors)
            messages.success(
                request, ' successful Registered ')
            # return render(request, 'base.html', {'name': 'ahmed', 'form': form})
            # rul = 1
            # return redirect('/')

        else:
            print('*'*100)
            print(form.is_valid())
            print(form.errors)
            print('#'*100)
            # messages.error(request, "Error")
            messages.error(
                request, ' Numberkaan horay ayuu ujiray')
            for errors in form.errors:
                print(errors)
            return render(request, 'base.html', {'name': 'ahmed', 'form': form})

    else:
        form = ExtentionsForm()

    form = ExtentionsForm()
    form2 = QueueForm()
    formall = {}
    formall['form'] = form
    formall['form2'] = form2

    return render(request, 'base.html', formall)

# Create your views here.


def add(request):
    return ""
