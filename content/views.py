from django.shortcuts import render, redirect
from content.models import StaticContent, Publication, PubType

# Create your views here.

def home_page(request):
	static_content = StaticContent.objects.get(purpose='home_text')
	recent_posts = Publication.objects.all().order_by('-date')[0:3]
	return render(request,'index.html',{'static_content' : static_content, 'recent_posts' : recent_posts})

def blog(request):
	pub_type = PubType.objects.get(type='Blog')
	content_posts = pub_type.publication_set.all().order_by('-date')
	return render(request,'blog_list.html',{'content_posts' : content_posts})

def blog_entry(request, blog_id):
	content_post = Publication.objects.get(id=blog_id)
	return render(request,'blog.html',{'content_post': content_post})

def projects(request):
	pub_type = PubType.objects.get(type='Projects')
	content_posts = pub_type.publication_set.all().order_by('-date')
	return render(request,'projects_list.html',{'content_posts' : content_posts})

def projects_entry(request,projects_id):
	content_post = Publication.objects.get(id=projects_id)
	return render(request,'projects.html',{'content_post': content_post})

def about(request):
	static_content = StaticContent.objects.get(purpose='about_text')
	return render(request,'about.html', {'static_content' : static_content})