from django.conf.urls import url, include
from django.contrib import admin
import tracker.views as tracker

urlpatterns = [
    url(r'^tracker/', include('tracker.urls')),
    url(r'^authorization/', include('authorization.urls')),
    url(r'^telephony/', include('telephony.urls')),
    url(r'^admin/', admin.site.urls),
    url(r'^$', tracker.trackers),
]
