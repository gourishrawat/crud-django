from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.


def index(request):
    return render(request,'index.html')

def login(request):
    if request.method=='POST':
        contact=request.POST['contact']
        email=request.POST['email']
        password=request.POST['password']
        if User.objects.filter(contact=contact).exists():
            if User.objects.filter(email=email).exists():
                if User.objects.filter(password=password).exists():
                    return render(request,'studentadd.html')
                else:
                    messages.error(request,'password was incorrect')
                    return redirect('/')
            else:
                messages.error(request,'email was incorrect')
                return redirect('/')
        else:
            messages.error(request,'contact was incorrect')
            return redirect('/')

def student(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        section=request.POST['section']
        school=request.POST['school']
        if Student.objects.filter(contact=contact).exists():
            messages.error(request,'contact is already exists')
            return redirect('/studentadd/')
        else:
            Student.objects.create(name=name,contact=contact,section=section,school=school)
            return redirect('/table/')

def table(request):
    data=Student.objects.all()
    return render(request,'table.html',{'data':data})

def edit(request,uid):
    uid=Student.objects.get(id=uid)
    return render(request,'edit.html',{'uid':uid})

def editdata(request):
    if request.method=='POST':
        id=request.POST['uid']
        name=request.POST['name']
        contact=request.POST['contact']
        section=request.POST['section']
        school=request.POST['school']
        Student.objects.filter(id=id).update(name=name,contact=contact,section=section,school=school)
        return redirect('/table/')

def delete(request,uid):
    Student.objects.filter(id=uid).delete()
    return redirect('/table/')