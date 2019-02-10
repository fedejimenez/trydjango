"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


from series.views import (
  series_listview,
  TVShowListView,
  TVShowDetailView,
  SeriesCreateView
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(), name='login'),
    path('', TemplateView.as_view(template_name='home.html')),
    path('series/', TVShowListView.as_view()),
    path('series/create', SeriesCreateView.as_view()),
    # path('series/<slug:name>', TVShowListView.as_view()),
    path('series/<slug>', TVShowDetailView.as_view()),
    # re_path(r'^series/(?P<slug>\w+)/$', TVShowListView.as_view()),
    path('about/', TemplateView.as_view(template_name='about.html')),
    path('contact/', TemplateView.as_view(template_name='contact.html'))
]
  