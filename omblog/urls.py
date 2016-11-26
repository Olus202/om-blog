from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
     url(r'^$', 'blog.views.home_page', name='home'),
     url(r'^post/(?P<pk>[0-9]+)/$', 'blog.views.post_view', name='post_view'),
     url(r'^all/$', 'blog.views.all_posts', name='all_posts'),
     url(r'^crown/$', 'blog.views.polish_crown', name='polish_crown'),
     url(r'^admin/', include(admin.site.urls)),
]
