
from django.contrib import admin
from django.conf.urls import include,url
from firstapp import views
urlpatterns = [
    url('^$',views.login_page,name='firstapp.login_page')
    
]
