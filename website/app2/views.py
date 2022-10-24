from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from .models import Register
from django.urls import reverse
from pymongo import MongoClient
def home(request):
    return HttpResponse("Welcome")

def template1(request):
    n = loader.get_template('first.html')
    return HttpResponse(n.render())

def context1(request):
    context={'name':'abcd'}
    return render(request,'second.html',context)

def urlparams(request,num1,num2):
    a=num1
    b=num2
    context={'a':a ,'b':b , 'c':a+b}
    return render(request,'third.html',context)

def reg(request):
    user = Register.objects.all().values()
    t = loader.get_template('data.html')
    context={
        'user': user,
    }
    return HttpResponse(t.render(context,request))

def add(request):
    d= loader.get_template('add.html')
    return HttpResponse(d.render({},request))

def addrecord(request):
    a = request.POST['fn']
    b = request.POST['ln']
    c = request.POST['us']
    d = request.POST['mail']
    sum= Register(FirstName=a,Lastname=b,Username=c,user_mail=d)
    sum.save()
    return HttpResponseRedirect(reverse('reg'))

def delete(request,id):
    a= Register.objects.get(id=id)
    a.delete()
    return HttpResponseRedirect(reverse('reg'))

def update(request,id):
        user = Register.objects.get(id=id)
        t = loader.get_template('update.html')
        context = {
            'user': user,
        }
        return HttpResponse(t.render(context, request))

def updaterecord(request,id):
    a= request.POST['fn']
    b= request.POST['ln']
    c= request.POST['us']
    d= request.POST['mail']
    up=Register.objects.get(id=id)
    up.FirstName=a
    up.Lastname=b
    up.Username=c
    up.user_mail=d
    up.save()
    return HttpResponseRedirect(reverse('reg'))

def sam(request):
    return render(request,'app2/form.html')

client = MongoClient("mongodb://localhost:27017/")
db = client['KL_U']
coll = db.CSE

def insert(request):
    if request.method=="POST":
        a = request.POST['us']
        b = request.POST['pass']
        coll.insert_one({'name': a, 'pass': b})
        return HttpResponse("Saved")
    return HttpResponse("NOT SAVED")



