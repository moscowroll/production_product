from django.shortcuts import render


from django.http import HttpResponse

def start(request):
    return render(request, 'start_view.html')
# Create your views here.


from identify.forms import Start_information

from . import models


def question_1(request):
    if request.method =="POST":

        form = Start_information(request.POST)
        if form.is_valid():
            form.save()
            login = request.POST.get("login")

            return render(request, 'question_1.html', {'login' : login})
        return render(request,'identify.html', {'form': form})


def question_2(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3"]:
            models.Person.objects.filter(login = login).update(answer_1= int(answer_number))

        return render(request, 'question_2.html', {'login' : login})



def question_3(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3", "4"]:
            models.Person.objects.filter(login = login).update(answer_2= int(answer_number))

        return render(request, 'question_3.html', {'login' : login})



def question_4(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2"]:
            models.Person.objects.filter(login = login).update(answer_3= int(answer_number))

        return render(request, 'question_4.html', {'login' : login})



def question_5(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3"]:
            models.Person.objects.filter(login = login).update(answer_4= int(answer_number))

        return render(request, 'question_5.html', {'login' : login})



def question_6(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3"]:
            models.Person.objects.filter(login = login).update(answer_5= int(answer_number))

        return render(request, 'question_6.html', {'login' : login})



def question_7(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3"]:
            models.Person.objects.filter(login = login).update(answer_6= int(answer_number))

        return render(request, 'question_7.html', {'login' : login})



def finish(request):
    if request.method =="POST":
        login = request.POST.get('login')
        print(login)
        answer_number = request.POST.get("answer_number", None)
        if answer_number in ["1", "2", "3"]:
            models.Person.objects.filter(login = login).update(answer_7= int(answer_number))

        return HttpResponse("Спасибо за прохождение теста!")
