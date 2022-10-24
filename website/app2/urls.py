from django.contrib import admin
from django.urls import path
from .views import home,template1,context1,urlparams,reg,add,addrecord,delete,update,updaterecord,insert,sam
urlpatterns = [
    path('home/',home,name='home' ),
    path('template/',template1,name='t'),
    path('context/',context1,name='c'),
    path('urlparam/<int:num1>/<int:num2>/',urlparams,name='url'),
    path('reg/',reg,name='reg'),
    path('reg/add/',add,name='add'),
    path('reg/add/addrecord/',addrecord,name='addrecord'),
    path('reg/delete/<int:id>',delete,name='delete'),
    path('reg/update/<int:id>',update,name='update'),
    path('reg/update/updaterecord/<int:id>',updaterecord,name='updaterecord'),
    path('insert/',insert,name='insert'),
    path('sign/',sam)
]