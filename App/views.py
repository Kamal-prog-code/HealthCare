from django.shortcuts import render
# Create your views here.
from django.shortcuts import render
from django.shortcuts import render, redirect 
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import pandas as pd
from .models import *
import joblib
from django.shortcuts import render,redirect
from django.template import Context, loader
from django.http import HttpResponse
from .forms import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User, auth
from django.contrib.auth.views import *
import pickle
import joblib
import os

def signup(request):
    if request.method == 'POST':
        stu = usersForm(request.POST)
        if stu.is_valid():
            user = User.objects.create_user(username=stu.cleaned_data['User_Name'],
                                            password=stu.cleaned_data['Password'],
                                            email=stu.cleaned_data['Email'])

            user.save()
            stu.save()
            return redirect('login')
    else:
        stu = usersForm()
    return render(request,'signup.html',{'form':stu})
from sklearn.linear_model import LogisticRegression
def login(request):
    if request.method == 'POST':
        user = User()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        context = {'user':request.user}
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request,'login.html',context)
    else:
        return render(request,'login.html')


def home(request):
	return render(request,'home.html')

def diab_test(request):
	if(request.method=='POST'):
		test=DiabTest()
		test.Pregnancies=float(request.POST.get('pg',None))
		test.Glucose=float(request.POST.get('gl',None))
		test.BP=request.POST.get('bp',None)
		test.Skinthickness=float(request.POST.get('st',None))
		test.Insulin=float(request.POST.get('ins',None))
		test.BMI=float(request.POST.get('bmi',None))
		test.Diabetic_pf=float(request.POST.get('dpf',None))
		test.age=float(request.POST.get('age',None))
		data=list((request.POST).dict().values())[1:]
		num_data=[i for i in data ]
		df_data=pd.DataFrame([num_data],columns=['Pregnancies', 'Glucose', 'BloodPressure', 'SkinThickness', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'])
		cls=joblib.load("prediction/dblogR.pkl")
		y_pred = cls.predict(df_data)[0]
		
		if(y_pred==0):
			str_res='Non Diabetic'
		else:
			str_res='Diabetic'
		print(str_res)
		test.user = str(request.user)
		test.Res=str_res
		test.save()
		return render(request,'diab_test.html',{'result':str_res})
	else:
		return render(request, 'diab_test.html')

def alz_test(request):
	return HttpResponse("Alz")


def heart_test(request):
	if(request.method=='POST'):
		test=HeartTest()
		test.age=float(request.POST.get('age',None))
		test.anaemia=float(request.POST.get('anaemia',None))
		test.creatinine_phosphokinase=float(request.POST.get('creatinine_phosphokinase',None))
		test.diabetes=float(request.POST.get('diabetes',None))
		test.ejection_fraction=float(request.POST.get('ejection_fraction',None))
		test.high_blood_pressure=float(request.POST.get('high_blood_pressure',None))
		test.platelets=float(request.POST.get('platelets',None))
		test.serum_creatinine=float(request.POST.get('serum_creatinine',None))
		test.serum_sodium=float(request.POST.get('serum_sodium',None))
		test.sex=float(request.POST.get('sex',None))
		test.smoking=float(request.POST.get('smoking',None))
		test.time=float(request.POST.get('time',None))
		test.user = str(request.user)
		data=list((request.POST).dict().values())[1:]
		num_data=[float(i) for i in data ]
		
		df_data=pd.DataFrame([num_data],columns=['age', 'anaemia', 'creatinine_phosphokinase', 'diabetes', 'ejection_fraction', 'high_blood_pressure', 'platelets', 'serum_creatinine','serum_sodium','sex','smoking','time'])
		final_model=joblib.load("prediction/heartknn.pkl")
		y_pred = final_model.predict(df_data)[0]
		print(num_data)
		print(y_pred)

		if(y_pred==1):
			str_res='There is a chance of heart failure in the feature.'
		else:
			str_res='No chance of getting heart failure as of now'
		print(str_res)
		test.DEATH_EVENT=y_pred
		test.save()
		return render(request,'heart_test.html',{'result':str_res})
	else:
		return render(request, 'heart_test.html')

def profile(request):
	heartT = HeartTest.objects.filter(user=str(request.user))
	diabT = DiabTest.objects.filter(user=str(request.user))
	return render(request,'profile.html',{'heartT':heartT,'diabT':diabT})





