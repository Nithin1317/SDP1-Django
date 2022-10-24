from django.urls import path
from . import views
urlpatterns = [
    path('',views.home),
    path('login/',views.login,name='login'),
    path('register/',views.register),
    path('about/',views.about),
    path('contact/',views.contact),
    path('medicines/',views.medicines),
    path('insert/',views.insert),
]
