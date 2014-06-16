from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from stats.views import CPUInfoViewSet, NetworkInfoViewSet, DOMElementCountViewSet, HomeView

admin.autodiscover()

router = routers.DefaultRouter()
router.register('cpu-info', CPUInfoViewSet)
router.register('network-info', NetworkInfoViewSet)
router.register('dom-element-count', DOMElementCountViewSet)


urlpatterns = patterns('',
    url(r'^$', HomeView.as_view()),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
)