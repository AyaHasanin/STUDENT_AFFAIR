from importlib.resources import path
from unicodedata import name
from django.urls import path
from . import views
urlpatterns =[
path('',views.home,name='home'),
path('add/',views.add,name='add'),
path('index/',views.index,name='index'),
path('activestudents/',views.activestudents,name='activestudents'),
path('inactivestudents/',views.inactivestudents,name='inactivestudents'),
path('add/addrecord/',views.addrecord,name='addrecord'),
path('index/delete/<int:id>',views.delete,name='delete'),
path('index/update/<int:id>',views.update,name='update'),
path('update/updaterecord/<int:id>',views.updaterecord,name='updaterecord'),
path('activeinactive/',views.activeinactive,name='activeinactive'),
path('department/',views.department,name='department'),
path('department/updatedepartment/<int:id>',views.updatedepartment,name='updatedepartment'),
path('updatedepartment/updatedeprecord,/<int:id>',views.updatedeprecord,name='updatedeprecord'),
]