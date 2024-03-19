from django.urls import path
# from django.urls import url
from myapp import views
from myapp.views import *

urlpatterns = [
path('',save_attendance,name='save_attendance'),
path('show_attendance',show_attendance,name='show_attendance'),
]
