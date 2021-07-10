from django.conf.urls import url
from django.db.models.query import ValuesIterable
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url('^upload/$',views.upload,name = 'upload'),
    url('^register/',views.register,name='register'),
    url('^login/',views.login,name='login'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)