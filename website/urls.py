from django.views import static
from django.conf.urls import include,url
from django.conf import settings

from website import views as website_views

urlpatterns = [
    url(r'^About/', website_views.about, name='about'),
    url(r'^Home/', website_views.index, name='index'),
]

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns.append(url(r'^media/(?P<path>.*)$', static.serve, {
        'document_root': settings.MEDIA_ROOT}))