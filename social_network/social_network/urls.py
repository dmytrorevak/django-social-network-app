"""social_network URL Configuration

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
from social_network_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.start_page_view, name='start_page'),
    url(r'^user/$', views.user_page_view, name='user_page'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^messages/([A-Za-z]*)$', views.messages_view, name='messages'),
    url(r'^friends/$', views.friends_view, name='friends'),
    url(r'^avatar/$', views.avatar_view, name='avatar'),
    url(r'^emojisPage/$', views.emojisPage_view, name='emojis'),
    url(r'^emojis/$', views.emojis2_view, name='emojis2'),
]
