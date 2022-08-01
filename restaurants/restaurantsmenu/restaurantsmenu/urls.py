"""restaurantsmenu URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path,include
from menu.views import SectionViews, ItemViews, ModifiersViews, MenuViews,IteamMapModifiersViews,NestIteamMapModifiersViews
from rest_framework import routers


rout = routers.DefaultRouter()
rout1 = routers.DefaultRouter()
rout2 = routers.DefaultRouter()

rout.register('section',SectionViews)
rout.register('item',ItemViews)
rout.register('modifiers',ModifiersViews)
#rout1.register('mapmodifier',NestIteamMapModifiersViews)
rout1.register('map-item-modifier',IteamMapModifiersViews,basename='map-item-modifier')
rout.register('menu',MenuViews,basename='menu')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include(rout.urls)),
    path('map/',include(rout1.urls)),
    # path('menu/',include(rout.urls)),

]
