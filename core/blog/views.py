from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import BlogPostModel,Category
from django.core.paginator import Paginator

# Create your views here.

def PostListView(request):
    posts = BlogPostModel.objects.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category = Category.objects.all()
    context = {
        'post' : page_obj,
        'category' : category
    }
    return render(request,'home.html',context)

def PostDetailView(request,slug):
    posts = BlogPostModel.objects.get(slug=slug)
    category = Category.objects.all()
    context = {
        'post' : posts,
        'category' : category
    }
    return render(request,'post.html',context)

def CategoryListView(request,slug):
    posts = Category.objects.get(slug=slug).catitems.all()
    paginator = Paginator(posts,5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category = Category.objects.all()
    context = {
        'post' : page_obj,
        'category' : category,
    }
    return render(request,'home.html',context)



       

