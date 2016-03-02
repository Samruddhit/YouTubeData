from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
from AppYouTubeData import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'YouTubeData.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.Login),
    url(r'^home/', views.Home),
    url(r'^loginAuthenticate/', views.LoginAuthentication),
    url(r'^logout/$', views.Logout),
    url(r'^dataFetcher/', views.FetchYouTubeData),
    url(r'^channelResult/', views.GetDataResult),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^getChannelData/$', views.GetChannelData.as_view(), name='GetChannelData'),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


