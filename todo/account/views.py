from django.shortcuts import render,redirect
from django.views import View
from .forms import RegForm,LogForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout


# Create your views here.

class LogView(View):
    def get(self,request):
        form=LogForm()
        return render(request,"log.html",{"form":form})
    def post(self,request):
        form=LogForm(data=request.POST)
        if form.is_valid():
            uname=form.cleaned_data.get('username')
            pswd=form.cleaned_data.get('password')
            user=authenticate(request,username=uname,password=pswd)
            if user:
                login(request,user)
                messages.success(request,"Login successfull")
                return redirect('list')
            else:
                return redirect('log')
        else:
            return render(request,"log.html",{"form":form})

class RegView(View):
    def get(self,request):
        form=RegForm()
        return render(request,"reg.html",{'form':form})
    def post(self,request):
        form_data=RegForm(data=request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"User Registration Successfull!!")
            return redirect('log')
        else:
            messages.error(request,"Registration Failed!!")
            return render(request,"reg.html",{"form":form_data})
class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect('log')