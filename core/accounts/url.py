from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import loginview,signupview
urlpatterns = [
    path('login/',loginview),
    path('signup/',signupview),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)