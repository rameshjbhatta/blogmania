"""
urls of the blogapp
"""
from django.db import router
from blogapp import views
from django.urls import include, path
from rest_framework import routers
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'bloginfos', views.BlogInfoViewSet)
router.register(r'contactinfos', views.ContactInfoViewSet)


urlpatterns = [
    path('', views.index, name='homepage'),
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
    path('aboutus', views.about, name='aboutuspage'),
    path('search', views.search, name='search'),
    path('contactus', views.contact, name='contactuspage'),
     path('blog/<int:blog_id>/', views.blog_detail, name='blog_detail'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
