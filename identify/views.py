from django.shortcuts import render

# Create your views here.
from . import forms

def identify(request):
    form = forms.Start_information()
    print(form)
    return render(request, 'identify.html', {"form": form})
