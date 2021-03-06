"""blog_project URL Configuration"""
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from blog_project import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
