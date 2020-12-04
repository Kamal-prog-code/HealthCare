from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='home'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('diab_test',views.diab_test,name='diab_test'),
    path('alz_test',views.alz_test,name='alz_test'),
    path('heart_test',views.heart_test,name='heart_test'),
]