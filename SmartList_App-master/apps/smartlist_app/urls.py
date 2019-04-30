from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^registration$', views.registration),
    url(r'^dashboard$', views.dashboard),
    url(r'^history$', views.history),
    url(r'^add_todo$', views.add_todo),
    url(r'^delete/(?P<id>\d+)$', views.delete_todo),
    url(r'^todo_done/(?P<id>\d+)$', views.todo_done),
    url(r'^delete/resource/(?P<id>\d+)$', views.delete_resource),
    # url(r'^upload/submit/$', views.image_load),
    url(r'^clean/history$', views.clean_history),
]
