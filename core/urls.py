from core.views import core_views
from django.conf.urls import url

__author__ = 'andrews'

urlpatterns = [
    url(r'^$', core_views.index, name='index'),
    url('contact', core_views.contact, name='contact'),
    # url('dashboard', core_views.dashboard, name='dashboard'),
    url('about', core_views.about,  name='about'),
    url('screena]', core_views.screen,  name='screen'),


    # url('account/login', user_views.sign_in, name='sign_in'),
    # url('account/logout', user_views.sign_out, name='logout'),
    # url('account/register', user_views.registration, name='registration'),
  ]
