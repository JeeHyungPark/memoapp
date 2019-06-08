from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Blog

# Create your views here.
def home(request): 
    blogs = Blog.objects
    return render(request, 'home.html', {'blogs': blogs})

def detail(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'detail.html', {'blog':blog_detail})

def new(request):
    return render(request, 'new.html')

def create(request):
    blog=Blog()
    blog.title=request.GET['title']
    blog.body=request.GET['body']
    blog.pub_date =timezone.datetime.now()
    blog.save()
    return redirect('/blog/'+str(blog.id))

def delete(request, blog_id):
    blog_detail = get_object_or_404(Blog, pk=blog_id)
    blog_detail.delete()
    return redirect('home')

def edit(request, blog_id):
    if(request.method == 'POST'):
        blog_detail = get_object_or_404(Blog, pk= blog_id)
        return render(request, 'edit.html', {'blog': blog_detail})

def update(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id)
    if(request.method == 'POST'):
        blog.title =request.POST['title']
        blog.body = request.POST['body']
        blog.save()
        return redirect('/blog/'+str(blog.id))