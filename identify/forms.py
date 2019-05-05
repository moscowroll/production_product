from django import forms

from start import models

class Start_information(forms.ModelForm):
    class Meta:
        model = models.Person
        fields = ('name',
                  'login',
                  'age',
                  'gender')
        labels = {
                  'name' : ("Имя"),
                  'login' : ("Логин"),
                  'age' : ("Возраст"),
                  'gender' : ("Пол")
            }
