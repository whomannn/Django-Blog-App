from django.urls import reverse
from django.db import models
from accounts.models import User
from django.shortcuts import redirect
# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50,null=False, unique=True) 
    def __str__(self):
        return self.title

class BlogPostModel(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True)
    category = models.ManyToManyField(Category, related_name='catitems')
    title = models.CharField(max_length=255)
    body = models.TextField()
    slug = models.SlugField(max_length=255,null=False, unique=True)
    background_image = models.ImageField(upload_to='post-images',blank=True)
    image1 = models.ImageField(upload_to='post-images',blank=True)
    image2 = models.ImageField(upload_to='post-images',blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('home')
    