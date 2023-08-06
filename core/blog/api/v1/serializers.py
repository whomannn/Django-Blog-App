from rest_framework import serializers
from blog.models import BlogPostModel,Category

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['title',]
class PostSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.email', read_only=True)
    # category = CategorySerializer(many=True)
    class Meta:
            model = BlogPostModel
            fields = ['author','category','title','body','slug','background_image','created_date']