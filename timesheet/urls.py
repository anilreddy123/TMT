from django.conf.urls import include, url,patterns
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    # Examples:
    # url(r'^$', 'timesheet.views.home', name='home'),
     url(r'^', include('Timemanagement.urls')),

    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)

