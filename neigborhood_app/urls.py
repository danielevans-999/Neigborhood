from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    
    path('', views.home, name='home'),
    path('single_hood/<int:id>/', views.single_neigborhood,name='single'),
    path('profile/', views.profile_info,name='profile'),
    path('update_profile/', views.update_profile,name='profileupdate'),
    path ('new_post/<int:id>/',views.new_post,name='newpost')
]


if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
