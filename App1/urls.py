
from django.urls import path, include
from . import views

app_name ="App1"

urlpatterns = [
    path('hai/<name>',views.hai,name="hai"),
    path('add/<num1>/<num2>',views.add,name="add"),
    path('temp/',views.demo,name="tempdemo"),
    path('temp2/',views.demo2,name="tempdemo2"),
    path('index/',views.index, name="index"),
    path('base/',views.base,name="base"),
    path('home/',views.hometemp,name="Homepage"),
    path('about/',views.abouttemp,name="about"),
    path('register/',views.register,name="register"),



]
