from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
# currently working
urlpatterns = [
      path('i18n/',include('django.conf.urls.i18n')),
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)