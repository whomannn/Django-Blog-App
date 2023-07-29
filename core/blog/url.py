from django.urls import path
from .views import PostListView,PostDetailView,CategoryListView
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('',PostListView),
    path('<slug>',PostDetailView),
    path('category/<slug>',CategoryListView)
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)