
from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('', views.start),
    path('identify/', include('identify.urls')),
    path('question_1/', views.question_1),
    path('question_2/', views.question_2),
    path('question_3/', views.question_3),
    path('question_4/', views.question_4),
    path('question_5/', views.question_5),
    path('question_6/', views.question_6),
    path('question_7/', views.question_7),
    path('finish/', views.finish)

]
