from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'drf_sample.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

#from rest_framework.routers import DefaultRouter
#from retails.views import ChainViewSet, StoreViewSet, EmployeeViewSet

#router = DefaultRouter()
#router.register(prefix='chains', viewset=ChainViewSet)
#router.register(prefix='stores', viewset=StoreViewSet)
#router.register(prefix='employees', viewset=EmployeeViewSet)

#urlpatterns = router.urls