from django.conf.urls import url

from tracker import views

urlpatterns = [
    url(r'^users/(?P<page>[0-9]+)/$', views.users, name='users_page'),
    url(r'^users/$', views.users, name='users'),
    url(r'^user_id_(?P<user_id>[0-9]+)/(?P<page>[0-9]+)$', views.user, name='user_page'),
    url(r'^user_id_(?P<user_id>[0-9]+)/$', views.user, name='user'),
    url(r'^tracker/(?P<track_id>[0-9]+)$', views.tracker, name='tracker'),
    url(r'^$', views.index, name='index'),
]
