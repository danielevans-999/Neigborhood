from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    
    url(r'^$', views.home, name='home'),
    url(r'^single_hood/(\d+)/$', views.single_neigborhood,name='single'),
    url(r'^profile/$', views.profile_info,name='profile'),
    url(r'^update_profile/$', views.update_profile,name='profileupdate'),
    url(r'^new_post/(\d+)/$',views.new_post,name='newpost'),
    url(r'^welcome_email/$', views.welcome_email,name='emails')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
