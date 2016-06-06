from django.conf.urls import url

from telephony import views

urlpatterns = [
    url(r'^clear_all/$', views.clear_all),
    url(r'^call_page/$', views.call_me_page, name='call_page'),
    url(r'^change_call/(?P<call_id>[0-9]+)$', views.change_call),
    url(r'^check_new_call/(?P<len_obj>[0-9]+)$', views.check_new_call),
    url(r'^add_call/(?P<user_id>[0-9]+)/(?P<tracker_id>[0-9]+)$', views.add_call),
]
