from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.review_list, name="review_list"),
    url(r'^$', views.review_list, name="review_list"),
    url(r'^stuff/$', views.review_list, name="review_list"),
    url(r'^(?P<id>\d+)/$', views.review_detail),
    url(r'^post/$', views.new_review, name='new_review'),
    url(r'^reviews/(?P<id>\d+)/edit$', views.edit_review, name='edit'),
]