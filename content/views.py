from django.shortcuts import render, redirect
from content.models import StaticContent, Publication, PubType

# Create your views here.

def home_page(request):
	static_content = StaticContent.objects.get(purpose='home_text')
	recent_posts = Publication.objects.all().order_by('-date')[0:3]
	return render(request,'index.html',{'static_content' : static_content, 'recent_posts' : recent_posts})

def blog(request):
	pub_type = PubType.objects.get(type='Blog')
	blog_posts = pub_type.publication_set.all().order_by('-date')
	return render(request,'blog.html',{'blog_posts': blog_posts})

def projects(request):
	pub_type = PubType.objects.get(type='Projects')
	projects_posts = pub_type.publication_set.all().order_by('-date')
	return render(request,'projects.html',{'projects_posts' : projects_posts})

def about(request):
	return render(request,'about.html')