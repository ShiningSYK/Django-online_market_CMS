from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('register', views.register),
    path('login', views.login),
    url(r'info/(?P<id>\d+)$',views.get_user_info),

    path('',views.add2cart),
    path('/deleteBatch',views.del_cart_items),
    url(r'/list/(?P<id>\d+)$',views.get_cart_list),
    url(r'/(?P<id>\d+)$',views.del_cart_item),
    path('/modify',views.modify),
]