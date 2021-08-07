
from django.conf.urls import url
from django.contrib import admin
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.hello),
    url(r'^translate/', views.translate,name='translate'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
