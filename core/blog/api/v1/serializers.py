from rest_framework import serializers
from blog.models import BlogPostModel
class PostSerializer(serializers.ModelSerializer):
    class Meta:
            model = BlogPostModel
            fields = ['author','category','title','body','slug','background_image','created_date']