from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # setting.py ni import qildik
from django.conf.urls.static import static
from django.views.generic.base import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', TemplateView.as_view(template_name='index.html'), name='home')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)