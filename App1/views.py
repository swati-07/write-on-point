from django.shortcuts import render,redirect
from .forms import Newpost,UserCreationFormUpdate
from .models import Blog
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required 
from datetime import datetime
import os
from django.conf import settings
# Create your views here.

def HomepageView(request):
	posts=Blog.objects.all()

	return render(request,"homepage.html",{"posts":posts})

def AboutView(request):
	return render(request,'about.html',{})
@login_required
def NewPostView(request):
	
	if request.method == 'POST':
		form=Newpost(request.POST,request.FILES)
		
		if form.is_valid():
			newblog=form.save()
			newblog.author=str(request.user)
			if 'publish' in request.POST:
				newblog.published=True
				newblog.publishtime=datetime.now()
				newblog.save()
			elif 'dontpublish' in request.POST:
				newblog.save()
		return redirect('home')
	else:
		form=Newpost()
		return render(request,'newpost.html',{'form':form})
@login_required
def DraftsView(request):
	objectsblog=Blog.objects.all().filter(published=False)
	objectsblog=objectsblog.filter(author=request.user)
	return render(request,'drafts.html',{'posts':objectsblog})


def DetailPostView(request,pk):
	post=Blog.objects.get(pk=pk)
	return render(request,'detailpost.html',{"post":post})
@login_required
def PostUpdateView(request,pk):
	post=Blog.objects.get(pk=pk)
	
	if request.method=='POST':
		form=Newpost(request.POST,request.FILES,instance=post)
		if form.is_valid:
			image_path=post.photo1.path
			if os.path.exists(image_path):
				os.remove(image_path)
			image_path2=post.photo2.path
			if os.path.exists(image_path2):
				os.remove(image_path2)
			form.author=str(request.user)
			form.save()

			return redirect('drafts')
	else:
		form=Newpost(instance=post)
	return render(request,'edit.html',{'form':form})
@login_required
def BlogpublishView(request,pk):
	post=Blog.objects.get(pk=pk)
	post.published=True
	post.publishtime=datetime.now()
	post.save()
	return redirect('home')
@login_required
def DeletePostView(request,pk):
	post=Blog.objects.get(pk=pk)
	post.delete()
	return redirect('home')
@login_required
def MyWorkView(request):
	posts=Blog.objects.all().filter(author=request.user).filter(published=True)
	return render(request,'mywork.html',{'posts':posts})

def RegisterView(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		form=UserCreationFormUpdate()
		if request.method=='POST':
			form=UserCreationFormUpdate(request.POST)
			if form.is_valid():
				form.save()
				return redirect('login')
		return render(request,'Accounts/register.html',{'form':form})

def LoginView(request):
	if request.user.is_authenticated:
		return redirect('home')
	else:
		if request.method=="POST":
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request,username=username,password=password)
			if user is not None:
				login(request,user)
				return redirect('home')
		return render(request,'Accounts/login.html',{})

def LogoutView(request):
	logout(request)
	return redirect('login')


