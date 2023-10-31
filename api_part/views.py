from django.shortcuts import render,redirect
# from rest_framework import viewsets
# from chunked_upload.views import ChunkedUploadView
from .models import Upload,Data
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required
import pandas as pd
import requests
from rest_framework.generics import ListAPIView
from .serializers import QuerySetSeializer
from rest_framework.response import Response
from .filters import DataFilter
from  django_filters.rest_framework import DjangoFilterBackend
# Create your views here.
def signup(request):
    if request.method == "POST":
        username=request.POST.get("username")
        password=make_password(request.POST.get("password"))
        user=User.objects.create(
            username=username,
            password=password
        )
        user.save()
        print("User Created")
        return redirect('login/')
    return render(request,"signup.html")

def login_user(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        print(username,password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            print("login success")
            return redirect('users')
        else:
            print("i=user is node")
    return render(request,"login_user.html")

def logout_user(request):
    logout(request)
    return render(request,"logout_user.html")

def convert_csv_to_model(file_path):
    database=pd.read_csv(file_path,delimiter=',')
    csv_file=[list(row) for row in database.values]
    for j in csv_file:
        Data.objects.create(
            name=j[1],
            domain=j[2],
            year_foundation=j[3],
            industry=j[4],
            sizerange=j[5],
            locality=j[6],
            country=j[7],
            linked_url=j[8],
            current_emp=j[9],
            total_emp=j[10]
        )
9
@login_required(login_url="login_user")
def upload(request):
    if request.method == "POST":
        uploaded_file = request.FILES.get('file', None)
        newfile=Upload.objects.create(file=uploaded_file)
        # newfile.save()
        convert_csv_to_model(newfile.file)
        print(uploaded_file.name,"saved successfully...")
        return redirect('builder')
    return render(request,"upload.html")

@login_required(login_url="login_user")
def Alldata(request):
    # name=request.GET.get("name")
    data=Data.objects.all()
    # if name:
    newfile=DataFilter(request.GET,queryset=data) 
    context={
        "filter":newfile

    }
    print(newfile.qs)
    return render(request,"Data.html",context)

@login_required(login_url="login_user")
def users(request):
    user=User.objects.all()
    return render(request,"users.html",context={"user":user})

class QuerySetView(ListAPIView):
    queryset=Data.objects.all()
    serializer_class=QuerySetSeializer
    filterset_fields= ['industry','year_foundation','locality','country','current_emp','total_emp']
    
def delete_user(request,username):
    try:
        user = User.objects.get(username=username)
        user.delete()
        return redirect('users')
    except User.DoesNotExist:
        return Response("User Not Exist")
    

