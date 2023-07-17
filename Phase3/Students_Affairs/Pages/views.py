from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .models import Members
from django.urls import reverse
from django.shortcuts import render

# Create your views here.
#def index(reqest):
    #template=loader.get_template('myfirst.html')
   # return HttpResponse(template.render())
#def index(request):
 #   return HttpResponse("Hello")
def index(reqest):
     mymembers=Members.objects.all().values()
     template =loader.get_template('index.html')
     context = {'mymembers': mymembers,}
     return HttpResponse(template.render(context,reqest))
def add(reqest):
    template=loader.get_template('add.html')
    return HttpResponse(template.render({},reqest))
def home(reqest):
    template=loader.get_template('home.html')
    return HttpResponse(template.render({},reqest))
def addrecord(reqest):
    x=reqest.POST['name']
    x1=reqest.POST['gender']
    x2=reqest.POST['gpa']
    x3=reqest.POST['email']
    x4=reqest.POST['phone']
    x5=reqest.POST['level']
    x6=reqest.POST['status']
    x7=reqest.POST['department']
    x8=reqest.POST['birth']
    member = Members(name=x,gender=x1,gpa=x2,email=x3,phone=x4,level=x5,status=x6,department=x7)
    member.save()
    return HttpResponseRedirect(reverse('home'))
def delete(request,id):
    member = Members.objects.get(id=id)
    member.delete()
    return HttpResponseRedirect(reverse('index'))
def update(request,id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('update.html')
    context = {'mymember':mymember,}
    return HttpResponse(template.render(context,request))
def updaterecord(reqest,id):
    x=reqest.POST['name']
    x1=reqest.POST['gender']
    x2=reqest.POST['gpa']
    x3=reqest.POST['email']
    x4=reqest.POST['phone']
    x5=reqest.POST['level']
    x6=reqest.POST['status']
    x7=reqest.POST['birth']
    member=Members.objects.get(id=id)
    member.name=x
    member.gender=x1
    member.gpa=x2
    member.email=x3
    member.phone=x4
    member.level=x5
    member.status=x6
    member.birth=x7
    member.save()
    return HttpResponseRedirect(reverse('update'))

# def department(request):
#     search_term=''
#     if 'search'in request.GET:
#         search_term=request.GET['search']
#         articles=Artical.objects.id().filter(feeder__icontains=search_term)
#     articles=Artical.objects.id()
#     return render(request,'Pages/department.html',{'articles':search_term})
def department(reqest):
     mymembers=Members.objects.all().values()
     template =loader.get_template('department.html')
     context = {'mymembers': mymembers,}
     return HttpResponse(template.render(context,reqest))
def updatedepartment(request,id):
    mymember = Members.objects.get(id=id)
    template = loader.get_template('updatedepartment.html')
    context = {'mymember':mymember,}
    return HttpResponse(template.render(context,request))
def updatedeprecord(reqest,id):
    x=reqest.POST['department']
    
    member=Members.objects.get(id=id)
    member.department=x
    member.save()
    return HttpResponseRedirect(reverse('updatedepartment')) 
def activestudents(request):
         #return render(request,'activestudents.html')#{'studet':Members.objects.filter(status='active')})
    mydata = Members.objects.filter(status='Active').values('name','id','status')
    template = loader.get_template('activestudents.html')
    context = {'student': mydata,}
    return HttpResponse(template.render(context, request))
def inactivestudents(request):
    mydata = Members.objects.filter(status='Inactive').values('name','id','status')
    template = loader.get_template('inactivestudents.html')
    context = {'student': mydata,}
    return HttpResponse(template.render(context, request))
def activeinactive(request):
    return render(request,'activeinactive.html')  
    
# def testing(request):
#     mydata = Members.objects.filter(status='Active').values('name','id','status')
#     template = loader.get_template('activestudents.html')
#     context = {'student': mydata,}
#     return HttpResponse(template.render(context, request))
# def testing(request):
#        mydata = Members.objects.filtter(status='Inactive').values_list('name','id','status')
#        template = loader.get_template('inactivestudents.html')
#        context = {
#       'mymembers': mydata,
#   }       
    