from django.conf.urls import include, url
from django.contrib import admin
from olive import views

urlpatterns = [
    # Examples:
    url(r'^$', views.home, name='home'),
    url(r'^burp/', views.get_details, name='burp'),

    url(r'^admin/', include(admin.site.urls)),
]
