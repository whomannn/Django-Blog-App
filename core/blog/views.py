from typing import Any
from django.db.models.query import QuerySet
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.views.generic import ListView,DetailView
from .models import BlogPostModel,Category
from django.core.paginator import Paginator
from .forms import PostForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.contrib import messages
from django.template import loader
from .mixins import FieldsMixin,AuthorAccesMixin
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

def PostListView(request):
    posts = BlogPostModel.objects.all()
    paginator = Paginator(posts,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category = Category.objects.all()
    context = {
        'post' : page_obj,
        'category' : category
    }
    return render(request,'home.html',context)


def CategoryListView(request,slug):
    posts = Category.objects.get(slug=slug).catitems.all()
    paginator = Paginator(posts,4)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    category = Category.objects.all()
    context = {
        'post' : page_obj,
        'category' : category,
    }
    return render(request,'home.html',context)
class create_post(FieldsMixin,LoginRequiredMixin,CreateView):
    model = BlogPostModel
    fields = ['author','title','body','category','background_image','slug']
    template_name = 'createpost.html'
    
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        
        return redirect('/blog/')
    
class update_post(FieldsMixin,AuthorAccesMixin,UpdateView):
    model = BlogPostModel
    fields = ['title','body','category','background_image']
    template_name = 'createpost.html'

class ArticleList(LoginRequiredMixin,ListView):
    template_name = 'articlelist.html'
    fields = ['author','title','body','category','background_image','slug']
    def get_queryset(self):
        return BlogPostModel.objects.filter(author=self.request.user)
class delete_view(LoginRequiredMixin,AuthorAccesMixin,DeleteView):
    model = BlogPostModel
    success_url = '/blog/articlelist/'