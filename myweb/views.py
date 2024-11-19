from django.shortcuts import render
from .models import EmpOperations
from pymongo import MongoClient
from urllib import request as rq
import json

def home(request):
    dic={}
    dic['developer']='yash project'
    dic['company']='wellcome to django'

    ct='london'
    response=rq.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=008414a67263a8db418b25e271fa2d9d")
    data=response.read()
    info=json.loads(data)
    des=info['weather'][0]['description']
        
    k=info['main']['feels_like']
    c=round(k-272.15,2)
    dic['city']=ct
    dic['desc']=des
    dic['feels']=c

    return render(request,"index.html",dic)

def login(request):
    page=None
    
    if request.method=="POST":
        id=request.POST.get("uid")
        ps=request.POST.get("psw")
        obj=EmpOperations()
        page=obj.checkuser(id,ps)

    return render(request,page)


def newemp(request):
    return render(request,"NewEmp.html")

def addemp(request):
    msg=None
    if request.method=="POST":
        try:
            no=int(request.POST.get("employeeNumber"))
            nm=request.POST.get("employeeName")
            dp=request.POST.get("department")
            lo=request.POST.get("location")
            po=request.POST.get("post")
            sl=float(request.POST.get("salary"))
            obj=EmpOperations()
            msg=obj.addnewemp(no,nm,dp,lo,po,sl)
        except:
            msg="Error in insert"
        
        dic={}
        dic['status']=msg
        
        return render(request,"NewEmpStatus.html",dic)


def searchno(request):
    dic={}
    if request.method=='POST':
        try:
            no=int(request.POST.get("empno"))
            obj=EmpOperations()
            dic=obj.serachonempno(no)
        except:
            print('error in search data')
    
    return render(request,"SearchResult.html",dic)


def allemp(request):
    obj=EmpOperations()
    data=obj.getallemp()
    return render(request,"ShReport.html",{'empdata':data})


def updsal(request):
    return render(request,"UpdateSalary.html")

def changesal(request):
    dic={}
    if request.method=="POST":
        try:
            no=int(request.POST.get("employeeNumber"))
            sal=float(request.POST.get("newSalary"))
            obj=EmpOperations()
            msg=obj.changesalary(no,sal)
            dic['status']=msg
        except:
            print('error')
            dic['status']='error in update'
    
            
    return render(request,"UpdateSalaryStatus.html",dic)

def delemp(request):
    return render(request,"DeleteEmp.html")

def delete(request):
    dic={}
    if request.method=="POST":
        try:
            no=int(request.POST.get("employeeNumber"))
            obj=EmpOperations()
            msg=obj.deleteemp(no)
            dic['status']=msg
        except Exception as e:
            print(e)
            dic['status']='error in delete'
    
    return render(request,"DeleteStatus.html",dic)


def elist(request):
    dic={}
    if request.method=="GET":
        loc=request.GET.get("loc")
        dic['location']=loc

    return render(request,"EmpLocationList.html",dic)

def searchfilm(request):
    return render(request,'SearchFilm.html')

def searchfilmonid(request):
    if request.method=="POST":
        fid=request.POST.get("filmid")
        dic={}
        dic["_id"]=fid
        print(dic)
        client=MongoClient("mongodb+srv://yashbajaj:Yash#$2000@yashcluster.krjhict.mongodb.net/?retryWrites=true&w=majority&appName=YashCluster")
        db=client["yashdb"]
        coll=db["films"]
        for film in coll.find(dic):
         print(film)

    return render(request,"filmdata.html",film)


def takecity(request):
    return render(request,"Takecity.html")

def showweather(request):
    if request.method=="POST":
        ct=request.POST.get("city")
        response=rq.urlopen("http://api.openweathermap.org/data/2.5/weather?q="+ct+"&appid=008414a67263a8db418b25e271fa2d9d")
        data=response.read()
        info=json.loads(data)
        des=info['weather'][0]['description']

        k=info['main']['feels_like']
        c=round(k-272.15,2)
        
        dic={}
        dic['city']=ct
        dic['desc']=des
        dic['feels']=c
    return render(request,"Showeather.html",dic)

