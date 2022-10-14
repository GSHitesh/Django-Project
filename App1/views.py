import re
from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage

# Create your views here.

def indexs(request):
    return HttpResponse('<h1>Welcome to itilite Sai Hitesh</h1>')

def hai(request,name):
    return HttpResponse('<h2> Hello {} </h1> ' .format(name)) 

def add(request,num1,num2):
    return HttpResponse('Sum of {} and {} is: {} ' .format(num1,num2,int(num1)+int(num2)))

def demo(request):
    fruits = ['Apple','Mango','Pineapple','Kiwi','Orange']
    return render(request,"index.html", context={"name":"Hitesh","Position":"ASE","fruits":fruits})

def demo2(request):
    return render(request,"Template2.html")

def index(request):
    return render(request,"index.html",context={"name":"Hitesh","Position":"ASE"})

def base(request):
    return render(request,"Base.html")

def hometemp(request):
    return render(request,"Pages/home.html")

def abouttemp(request):
    return render(request,"Pages/about.html")

def register(request):
    if request.method == "POST":
        firstname = request.POST.get("firstname")
        middlename = request.POST.get("middlename")
        lastname = request.POST.get("lastname")
        course = request.POST.get("course")
        gender = request.POST.get("gender")
        phone = request.POST.get("phone")
        address = request.POST.get("address")
        if request.FILES:
            file = request.FILES['profilepic']
            fs = FileSystemStorage()
            savedfile = fs.save(file.name,file)
            file_url = fs.url(savedfile)

        return HttpResponse('Received Data is {},{},{},{},{},{},{},<img src = {}>' 
        .format(firstname,middlename,lastname,course,gender,phone,address,file_url))
    return render(request,"Pages/register.html")