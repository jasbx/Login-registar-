
from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth import logout,login
from .models import *

from .form import *

from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.


# =======================================================================================
# {regestar}

def regs(request):
    form=Loginform()
    if request.method=='POST':
      form=Loginform(request.POST)
      if form.is_valid():
            form.save()
           
            messages.success(request,"create user succsessfully")
            return redirect('login')
    context={'form':form}
    return render (request,'regstar.html',context=context)
# ===========================================================================================

def login_user(request):
        form=Loginform()
        if request.method=='POST':

          username=request.POST.get('username')
          password=request.POST.get('password1')
          user=authenticate(request,username=username,password=password)
          form=Loginform(request.POST)
          if user is not None:
                login(request,user)
                return redirect('home')
        else:
            messages.info(request,"the user or password not corecct")
        
        context={'form':form}
        return render (request,'login.html',context=context)
# ==============================================={logout}
@login_required(login_url='login')
def logout_user(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')

def home(request):
    return render (request,'home.html')
