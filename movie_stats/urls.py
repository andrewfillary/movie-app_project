from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^stats/$', views.all_statistics, name='statistics'),
    url(r'^stats/(?P<id>\d+)/$', views.review_detail),
    url(r'^new_movie/$', views.new_movie, name='new_movie'),
]

