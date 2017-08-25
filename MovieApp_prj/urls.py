"""MovieApp_prj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from magazines import views as magazine_views
from django.views.static import serve
from settings.dev import MEDIA_ROOT
from settings.staging import STATIC_ROOT
from accounts import views as accounts_views
from Hello import views as hello_views


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello_views.get_magazine_and_review, name='index'),
    url(r'', include('movie_stats.urls')),
    url(r'^subscribe/$', accounts_views.payment_method, name='payment_method'),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^magazines/$', magazine_views.all_magazines, name='magazines'),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),
    url(r'^cancel_subscription/$', accounts_views.cancel_subscription, name='cancel_subscription'),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^about/$', hello_views.get_about_page, name='about'),
    url(r'^contact/$', hello_views.get_contact_page, name='contact'),

]
