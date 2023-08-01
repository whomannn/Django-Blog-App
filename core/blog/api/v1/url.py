from django.urls import path
from .views import ListPostApi,UpdatePostApi
urlpatterns = [
    path('articlelist/',ListPostApi.as_view()),
    path('update/<slug>/',UpdatePostApi.as_view()),
] 
