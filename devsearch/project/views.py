from django.shortcuts import render,redirect
from .models import project
from .forms import addProjectForm
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


# Create your views here.
def  loginUser(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        try:
            user=User.objects.get(username=username)
        except:
            print("user does not exist")
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            print("username or password incorrect")
    return render(request,'project/login_register.html')    

def logoutUser(request):
    logout(request)
    return redirect("login")

def registerUser(request):
    page="register"
    form=UserCreationForm()
    if request.method=='POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            user=form.save(commit=False)
            user.username=user.username.lower()
            user.save()
            login(request,user)
            return redirect('home')
    return render(request,'project/login_register.html',{"page":page,"form":form})

def viewproject(request):
    projects=project.objects.all()
    return render(request,"project/view.html",{"projects":projects})

@login_required(login_url='login')
def viewSingleProject(request,pk):
    projectsingle=project.objects.get(id=pk)
    return render(request,"project/viewproject.html",{"project":projectsingle})

@login_required(login_url='login')
def addproject(request):
    form=addProjectForm()
    if request.method=="POST":
        form=addProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,"project/addproject.html",{"form":form})

@login_required(login_url='login')
def editProject(request,pk):
    editproject=project.objects.get(id=pk)
    form=addProjectForm(instance=editproject)
    if request.method=="POST":
        form=addProjectForm(request.POST,instance=editproject)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request,"project/editproject.html",{"form":form})

@login_required(login_url='login')
def deleteProject(request,pk):
    deleteproject=project.objects.get(id=pk)
    deleteproject.delete()
    return viewproject(request)
    
