from django.forms import ModelForm, Textarea
from django.db import models

# Create your models here.


class Students(models.Model):
    f_name = models.CharField(max_length=100)
    l_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    # def __str__(self):
    #     return self.f_name, self.email


# class Meta:
#     db_table = 'students'
