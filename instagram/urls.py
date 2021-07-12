from django.conf.urls import url
from django.urls.conf import include,include
from django.db.models.query import ValuesIterable
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.welcome,name = 'welcome'),
    url(r'^upload/$',views.upload,name = 'upload'),
    url(r'^uploadImage/$',views.uploadImage,name = 'uploadImage'),
    url(r'^register/$',views.register,name='register'),
    url(r'^login',views.loginpage,name='loginpage'),
    url(r'^logout/&',views.logout,name='logout'),
    url(r'^profile/&',views.profilepage,name='profilepage'),
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^like/', views.like, name='like'),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)