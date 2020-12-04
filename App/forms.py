from django import forms
from .models import *

class usersForm(forms.ModelForm):
    class Meta:
        model = users
        fields = ['User_Name','Email','Password']

class TestForm(forms.ModelForm):
    class Meta:
        model = DiabTest
        fields = ['Pregnancies','Glucose','BP','Skinthickness','Insulin','BMI','Diabetic_pf','age']