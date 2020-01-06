"""instagram URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin


from django.contrib.auth import views
from django.urls import path, include
from gram.views import account

from account.views import login_view, register_view,logout_view
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('gram.urls')),
    path('',account),
    path('account/login/',login_view),
    path('account/register/',register_view),
    path('account/logout/',logout_view),
    path('tinymce/',include('tinymce.urls')),
   
    path('accounts/',include('registration.backends.simple.urls')),
    path('logout/',views.logout,{"next_page":'/'}),
    

]
