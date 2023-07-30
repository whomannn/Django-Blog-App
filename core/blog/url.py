from django.urls import path
from .views import PostListView,PostDetailView,CategoryListView
from comment.views import coment_view
from django.conf import settings
from django.conf.urls.static import static
from accounts.views import loginview
urlpatterns = [
    path('',PostListView),
    path('<slug>',PostDetailView,),
    path('category/<slug>',CategoryListView),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)