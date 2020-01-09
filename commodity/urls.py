from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('list', views.list),
    url(r'tree/(?P<id>\d+)$', views.get_category_tree),
    url(r'(?P<id>\d+)$', views.get_by_id),

    path('gettree/',views.get_tree)
]
