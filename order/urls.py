from django.urls import path
from . import views
from django.conf.urls import url
urlpatterns = [
    path('',views.order),
    url(r'/detail/(?P<id>\d+)$',views.get_order_detail),
    url(r'/(?P<id>\d+)$',views.get_order)
]