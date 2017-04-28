from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

from e_commerce import settings

urlpatterns = [
                  url(r'^', include('shop.urls')),
                  url(r'^admin/', include(admin.site.urls)),
                  url(r'^auth/', include('loginsys.urls')),
                  url(r'^shop/', include('shop.urls')),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
