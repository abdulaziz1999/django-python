from django import forms
from students.models import Students
from .models import *


class StudentsFrom(forms.ModelForm):
    class Meta:
        model = Students
        fields = "__all__"
