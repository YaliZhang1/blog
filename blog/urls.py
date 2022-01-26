from django.conf.urls import url
from blog import views

from blog import views

app_name='blog'

urlpatterns = [
    url(r'^$', views.index, name="index"),

    url(r'^category/(?P<category>\w+)/', views.index, name="category"),
    url(r"^user/(?P<user>\w+)/", views.index),
    url(r'^home/', views.home, name="home"),

    url("edit/(?P<pk>\d*)?", views.edit, name="edit"),
    url(r'^view/(?P<id>\d+)', views.view, name="view"),
    
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.user_login, name="login"),
    url(r'^logout/', views.user_logout, name='logout'),
]

