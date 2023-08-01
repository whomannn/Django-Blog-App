from django.urls import path
from .views import PostListView,CategoryListView,create_post,update_post,ArticleList,delete_view
from comment.views import coment_view
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import loginview

urlpatterns = [
    path('',PostListView,name='home'),
    path('<slug>',coment_view),
    path('category/<slug>',CategoryListView),
    path('createpost/',create_post.as_view()),
    path('editpost/<slug>',update_post.as_view()),
    path('deletepost/<slug>',delete_view.as_view(),name='deletepost'),
    path('articlelist/',ArticleList.as_view()),
    

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)