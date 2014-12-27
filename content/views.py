from django.shortcuts import render, redirect
from content.models import StaticContent, Publication

# Create your views here.

def home_page(request):
	return render(request,'index.html')

def blog(request):
	return render(request,'blog.html')

def projects(request):
	return render(request,'projects.html')

def about(request):
	return render(request,'about.html')