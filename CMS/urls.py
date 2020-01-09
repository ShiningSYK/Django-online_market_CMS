"""CMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .settings import MEDIA_ROOT
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('commodity/', include('commodity.urls')),
    path('eshop/',include([
        path('order',include('order.urls')),
        path('cart',include('user.urls')),
        path('user/',include('user.urls')),
        path('activity/',include('activity.urls')),
        path('product/',include('commodity.urls')),
        path('category/',include('commodity.urls'))
    ])),

    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
]
