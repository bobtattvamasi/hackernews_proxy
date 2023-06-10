"""hackernews_proxy URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
# Path: hackernews_proxy/urls.py
from django.urls import path
from hackernews import views
from hackernews.proxy import HackerNewsProxy
from django.conf.urls.static import static
from . import settings
from django.contrib import admin

proxy = HackerNewsProxy()

urlpatterns = [
    path('', proxy.proxy_home, name='proxy_home'),
    path('newest/', views.newest, name='newest'),
    path('news/', proxy.proxy_home, name='news'),
    path('item/news/', proxy.proxy_home, name='news'),
    path('item/', proxy.proxy_item, name='proxy_item'),
    path('admin/', admin.site.urls),

    path('from/', views.from_site, name='from'),
    path('user/', views.user, name='user'),
    path('front/', views.past, name='past'),
    path('newcomments/', views.newcomments, name='newcomments'),
    path('ask/', views.ask, name='ask'),
    path('show/', views.show, name='show'),
    path('jobs/', views.jobs, name='jobs'),
    path('submit/', views.submit, name='submit'),
    path('login/', views.login, name='login'),

    path('newsguidelines.html', views.newsguidelines, name='newsguidelines'),
    path('newsfaq.html', views.newsfaq, name='newsfaq'),
    path('lists/', views.lists, name='lists'),
    path('security.html', views.security, name='security'),
    path('legal/', views.legal, name='legal'),
    path('apply/', views.apply, name='apply'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)