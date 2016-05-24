from django.conf.urls import url
from authorization import views
urlpatterns = [
    url(r'^login/$', views.login),
    url(r'^logout/$', views.logout),
    url(r'^registration/$', views.reg),
    url(r'^reg_new_user/$', views.add_reg)
]
