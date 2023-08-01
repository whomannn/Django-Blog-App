from rest_framework.generics import (
    ListAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from blog.models import BlogPostModel
from .serializers import PostSerializer
from blog.mixins import AuthorAccesMixin
from django.contrib.auth.mixins import LoginRequiredMixin

class ListPostApi(LoginRequiredMixin,ListCreateAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = PostSerializer
class UpdatePostApi(AuthorAccesMixin,RetrieveUpdateDestroyAPIView):
    queryset = BlogPostModel.objects.all()
    serializer_class = PostSerializer
    lookup_field = 'slug'
