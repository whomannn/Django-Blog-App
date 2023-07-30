from django.http import HttpResponse, HttpResponseRedirect
from .forms import CommentForm
from .models import Comment
from django.contrib import messages
from blog.models import BlogPostModel
from django.template import loader
def coment_view(request,slug):
    template = loader.get_template("post.html")
    if request.method == "POST":
        if request.user.is_authenticated:
            CommentForm_var = CommentForm(request.POST)
            if CommentForm_var.is_valid():
                post = BlogPostModel.objects.get(slug=slug)
                author = request.user
                content = CommentForm_var.cleaned_data['content']
                Comment.objects.create(content=content,author=author,post=post)
                return HttpResponseRedirect('/blog/'+slug)
        else:
            messages.error(request,"برای نظر دادن وارد شوید")
            CommentForm_var = CommentForm()
            context = {
                'comment' : CommentForm_var
            }
            return HttpResponse(template.render(context,request))
    else:
        CommentForm_var = CommentForm()
        # comment_list = Comment.objects.filter(slug = slug)
        # paginator = Paginator(comment_list,20)
        # page_number = request.GET.get("page")
        # page_obj = paginator.get_page(page_number)
        context = {
            'comment' : CommentForm_var,
            # 'comments' : comment_list
        }
        return HttpResponse(template.render(context,request))