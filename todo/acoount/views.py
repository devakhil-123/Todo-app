from django.shortcuts import render,redirect
from django.views.generic import View
from .forms import todoForm
from .models import todoModel
from django.contrib import messages

class HomeView(View):
    def get(self,request):
        todo=todoModel.objects.all()
        return render(request,"list.html",{"data":todo})

class WorkView(View):
    def get(self,request):
        form=todoForm()
        return render(request,"add.html",{"form":form})

    def post(self,request):
        form_data=todoForm(data=request.POST,files=request.FILES)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"todo added successfullly!!")
            return redirect('list')
        else:
            messages.error(request,"todo adding failed")
            return render(request,"add.html",{"form":form_data})


class TododeleteView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get("id")
        data=todoModel.objects.get(id=tid)
        data.delete()
        messages.info(request,"todo deleted successfully")
        return redirect("list")
class TodoeditView(View):
    def get(self,request,**kwargs):
        tid=kwargs.get('id')
        todo=todoModel.objects.get(id=tid)
        form=todoForm(instance=todo)
        return render(request,"edit.html",{"form":form})
    def post(self,request,**kwargs):
        tid=kwargs.get(id=tid)
        form_data=todoForm

class TodolistView(View):
    def get(self,request):
        to=todoModel.objects.all()
        return render(request,"list.html",{"data":to})