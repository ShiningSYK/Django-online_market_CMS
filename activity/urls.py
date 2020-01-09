from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    url(r'status/(?P<status>\d+)$', views.get_commodities),
    url(r'(?P<id>\d+)$',views.get_activities),
]