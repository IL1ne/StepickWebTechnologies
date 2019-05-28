# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'login/?', auth_views.login, name='login'),
    url(r'signup/?', views.signup, name='signup'),
    url(r'logout/?', auth_views.logout, name='logout'),
    url(r'question/(?P<id_question>.+)?/', views.show_question,
        name='show_question'),
    url(r'ask/?', views.ask, name='ask'),
    url(r'popular/?', views.popular, name='popular'),
    # url(r'new/?', views.new, name='new'),
    # url(r'/\?page=(?P<page>\d+)', views.home, name='home'),
    url(r'', views.home, name='home'),
]
