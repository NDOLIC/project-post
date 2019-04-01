
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    url('^$',views.home,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post/(\d+)',views.post,name ='post') ,
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^edit_profile/(\d+)',views.edit_profile,name ='edit_profile') ,
    url(r'^profile/(\d+)',views.profile,name ='profile') ,
    
   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
