from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^api/Pins', view=views.AllPins, name="api_all_pins"),
    url(r'^api/Pins/(?P<id>[0-9]+)$', view=views.Pin_update, name="api_pin_update"),
    url(r'^api/trending/(?P<k>[0-9]+)$', view=views.TrendingPins, name="api_trending_pins"),
]