from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

from Bank import views
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'untitled1.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', TemplateView.as_view(template_name='login.html')),
    url(r'^main/$', views.main_view, name='main'),
    url(r'^category/(?P<category_slug>[-\w]+)/$', views.category_view, name='category'),
    url(r'^product/(?P<product_slug>[-\w]+)/$', views.product_view, name='product'),
    url(r'^login_page/$', views.login_page, name='login_page'),
    url(r'^login/$', views.loginprocess, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^register/$', views.reg_view.as_view(), name='register'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
       {'document_root': settings.MEDIA_ROOT}),
)
