from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from stats.views import CPUInfoViewSet, NetworkInfoViewSet, DOMElementCountViewSet, HomeView, CookieViewSet

admin.autodiscover()

router = routers.DefaultRouter()
router.register('cpu', CPUInfoViewSet)
router.register('network', NetworkInfoViewSet)
router.register('dom', DOMElementCountViewSet)
router.register('cookie', CookieViewSet)


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)
