from django.core.mail import mail_admins
from django.shortcuts import render
from django.http.response import HttpResponse,HttpResponseRedirect
from pymongo import MongoClient
from django.urls import reverse
# Create your views here.
def home(request):
    return render(request,'my_app/home.html')
def login(request):
    return render(request,'my_app/login.html')
def register(request):
    return render(request,'my_app/registrationfrom.html')
def about(request):
    return render(request,'my_app/about.html')
def contact(request):
    return render(request,'my_app/contact.html')
def medicines(request):
    return render(request,'my_app/medicines.html')

client = MongoClient("mongodb://localhost:27017/")
db = client['SDP1']
coll = db.CSE

def insert(request):
    if request.method == 'POST':
        a = request.POST['username']
        b = request.POST['fname']
        c = request.POST['lname']
        d = request.POST['email']
        e = request.POST['pass1']
        coll.insert_one({"FirstName":b,"LastName":c,"Username":a,"Email":d,"Password":e})
        return HttpResponseRedirect(reverse('login'))