
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
   
    url('^$',views.home,name='home'),
    url(r'^new/post$', views.new_post, name='new-post'),
    url(r'^post/(\d+)',views.post,name ='post') ,
    url(r'^like_home/(\d+)',views.like_home,name ='like1') ,
    url(r'^like_post/(\d+)',views.like_post,name ='like2') ,
    url(r'^new_comment/(\d+)',views.add_comment,name ='comment') ,
    url(r'^search/', views.search_results, name='search_results'),
    url(r'^edit_profile/(\d+)',views.edit_profile,name ='edit_profile') ,
    url(r'^profile/(\d+)',views.profile,name ='profile') ,
    url(r'^follow/(\d+)',views.follow_profile,name ='follow') ,
    url(r'^unfollow/(\d+)',views.unfollow_profile,name ='follow') ,
    url(r'^followers/(\d+)',views.who_followers,name ='followers') ,   
    url(r'^following/(\d+)',views.who_following,name ='following') , 

   
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
