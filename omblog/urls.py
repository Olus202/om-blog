from django.conf.urls import url
#from django.contrib import admin

urlpatterns = [
     url(r'^$', 'blog.views.home_page', name='home'),
]
