from django.conf.urls import url

from tracker import views

urlpatterns = [
    url(r'^trackers/(?P<page>[0-9]+)$', views.trackers, name='trackers_page'),
    url(r'^trackers/$', views.trackers, name='trackers'),
    url(r'^(?P<track_id>[0-9]+)$', views.tracker, name='tracker'),
    url(r'^confirm_tracker/(?P<track_id>[0-9]+)$', views.confirm, name='confirm'),
    url(r'^$', views.trackers, name='index'),
]
