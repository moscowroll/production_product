# from django.shortcuts import render
#
#
# from django.http import HttpResponse
#
# from identify.forms import Start_information
#
#
# from . import forms
#
# def question_1(request):
#     if request.method =="POST":
#
#         form = Start_information(request.POST)
#         if form.is_valid():
#             form.save()
#             login = request.POST.get("login")
#
#             return render(request, 'question_1.html', {'login' : login})
#
#
#
# def question_2(request):
#     if request.method =="POST":
#         login = request.POST.get('login')
#         print(login)
#         answer_number = request.POST.get("answer_number", None)
#         if answer_number in ["1", "2"]:
#             models.User_and_Answers.objects.filter(login = login).update(answer_1= int(answer_number))
#
#         # return render(request, 'question_2.html', {'login' : login})
#         return HttpResponse("Solo")
