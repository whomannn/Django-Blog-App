from django.http import Http404
from django.shortcuts import get_object_or_404
from blog.models import BlogPostModel,Category
class FieldsMixin():
    def dispatch(self,request,*args, **kwargs):
        if request.user.is_superuser:
            self.fields = ['author','title','body','category','background_image','slug']
        else:
            self.fields = ['title','body','category','background_image','slug']
        return super().dispatch(request,*args, **kwargs)
    
class AuthorAccesMixin():
    def dispatch(self,request,slug,*args, **kwargs):
        article = get_object_or_404(BlogPostModel,slug=slug )
        if article.author == request.user or request.user.is_superuser :
            return super().dispatch(request,*args, **kwargs)
        else:
            raise Http404('you cant edit this post(you are not author of this post)')
        
# class CategoryTitleMixin():
#     def dispatch(self,request,*args, **kwargs):
#         article = get_object_or_404(BlogPostModel)
#         print(article.category)
#         return super().dispatch(request,*args, **kwargs)
