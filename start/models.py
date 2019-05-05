from django.db import models



BOOL_CHOICES = ((True, 'Мужской'), (False, 'Женский'))


class Person(models.Model):
    name = models.CharField(max_length = 20)
    age = models.IntegerField()
    gender = models.BooleanField(choices=BOOL_CHOICES, default=True)
    # gender = models.CharField(max_length = 10)
    login = models.CharField(max_length=20, unique= True)

    answer_1 = models.IntegerField(default = 0 )
    answer_2 = models.IntegerField(default = 0 )
    answer_3 = models.IntegerField(default = 0 )
    answer_4 = models.IntegerField(default = 0 )
    answer_5 = models.IntegerField(default = 0 )
    answer_6 = models.IntegerField(default = 0 )
    answer_7 = models.IntegerField(default = 0 )
# Create your models here.
